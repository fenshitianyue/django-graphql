# -*- coding:UTF-8 -*-

from graphene_django import DjangoObjectType
import graphene

from mygraphdata.models import User as Users

class UserType(DjangoObjectType):
    class Meta:
        model = Users

# 查询
class Query(graphene.ObjectType):
    # List 返回结果会是遍历所有查询结果
    users = graphene.List(UserType)
    # Field 返回结果只存在单个(其中可以添加参数：ex、pk)
    single_user = graphene.Field(UserType, pk=graphene.String())  # 通过名字来获取指定数据
    # 定义函数名的格式：resolve_字段
    # **kwargs 传递参数
    # pk:如果在字段中定义，则方法参数中必须包含

    def resolve_users(self, info, **kwargs):
        return Users.objects.all()

    def resolve_single_user(self, info, pk):
        return Users.objects.get(name=pk)

# 添加
class CreateUser(graphene.Mutation):
    class Input:
        Name = graphene.String()
        Title = graphene.String()
        Content = graphene.String()
        # pushed_at =
    info = graphene.Field(UserType)
    ok = graphene.Boolean()

    def mutate(self, info, **kwargs):
        user_obj = Users(name=kwargs['Name'], title=kwargs['Title'], content=kwargs['Content'])
        try:
            user_obj.save()
            ok = True
        except Exception as e:
            print e
            ok = False
        return CreateUser(ok=ok, info=user_obj)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


# 修改
# 删除

schema = graphene.Schema(query=Query, mutation=Mutation)



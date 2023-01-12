import graphene
from graphene_django import DjangoObjectType
from .models import Category, Book, Order, Client, Delivery, BookHasOrder, Review


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'description',
            'books_amount'
        )


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = (
            'id',
            'author',
            'title',
            'category',
            'price',
            'amount',
            'description',
            'page_amount',
            'owner'
        )


class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = (
            'id',
            'first_name',
            'surname',
            'address',
            'birthdate',
            'phone_number',
            'bank_account',
            'email',
            'password'
        )


class DeliveryType(DjangoObjectType):
    class Meta:
        model = Delivery
        fields = (
            'id',
            'price',
            'type',
            'time',
            'priority'
        )


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = (
            'id',
            'client',
            'delivery',
            'quantity',
            'price',
            'address',
            'phone',
            'date',
            'status'
        )


class BookHasOrderType(DjangoObjectType):
    class Meta:
        model = BookHasOrder
        fields = (
            'id',
            'order',
            'book',
        )


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        fields = (
            'id',
            'client',
            'book',
            'scale_points',
            'read_date',
            'advantages',
            'disadvantages',
            'recommend',
            'read_again'
        )


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    books = graphene.List(BookType)
    clients = graphene.List(ClientType)
    deliveries = graphene.List(DeliveryType)
    orders = graphene.List(OrderType)
    book_has_orders = graphene.List(BookHasOrderType)
    reviews = graphene.List(ReviewType)

    def resolve_books(root, info, **kwargs):
        # Querying a list
        return Book.objects.all()

    def resolve_categories(root, info, **kwargs):
        # Querying a list
        return Category.objects.all()

    def resolve_clients(root, info, **kwargs):
        # Querying a list
        return Client.objects.all()

    def resolve_deliveries(root, info, **kwargs):
        # Querying a list
        return Delivery.objects.all()

    def resolve_orders(root, info, **kwargs):
        # Querying a list
        return Order.objects.all()

    def resolve_book_has_orders(root, info, **kwargs):
        # Querying a list
        return BookHasOrder.objects.all()

    def resolve_reviews(root, info, **kwargs):
        # Querying a list
        return Review.objects.all()


class CategoryInput(graphene.InputObjectType):
    title = graphene.String()
    description = graphene.String()
    books_amount = graphene.String()


class CreateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, input):
        category = Category()
        category.title = input.title
        category.description = input.description
        category.books_amount = input.books_amount
        category.save()
        return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInput(required=True)
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, input, id):
        category = Category.objects.get(pk=id)
        category.title = input.title
        category.description = input.description
        category.books_amount = input.books_amount
        category.save()
        return UpdateCategory(category=category)


class BookInput(graphene.InputObjectType):
    title = graphene.String()
    category = graphene.String()
    author = graphene.String()
    price = graphene.String()
    amount = graphene.String()
    page_amount = graphene.String()
    description = graphene.String()
    owner = graphene.String()


class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, input):
        book = Book()
        book.title = input.title
        book.category = input.category
        book.author = input.author
        book.price = input.price
        book.amount = input.amount
        book.page_amount = input.page_amount
        book.description = input.description
        book.order = input.order
        book.save()
        return CreateBook(book=book)


class UpdateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)
        id = graphene.ID()

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, input, id):
        book = Book.objects.get(pk=id)
        book.title = input.title
        book.category = input.category
        book.author = input.author
        book.price = input.price
        book.amount = input.amount
        book.page_amount = input.page_amount
        book.description = input.description
        book.order = input.order
        book.save()
        return UpdateBook(book=book)


class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

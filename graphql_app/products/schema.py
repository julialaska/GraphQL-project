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


class DeliveryInput(graphene.InputObjectType):
    price = graphene.String()
    type = graphene.String()
    time = graphene.String()
    priority = graphene.String()


class CreateDelivery(graphene.Mutation):
    class Arguments:
        input = DeliveryInput(required=True)

    delivery = graphene.Field(DeliveryType)

    @classmethod
    def mutate(cls, root, info, input):
        delivery = Delivery()
        delivery.price = input.price
        delivery.type = input.type
        delivery.time = input.time
        delivery.priority = input.priority
        delivery.save()
        return CreateDelivery(delivery=delivery)


class UpdateDelivery(graphene.Mutation):
    class Arguments:
        input = DeliveryInput(required=True)
        id = graphene.ID()

    delivery = graphene.Field(DeliveryType)

    @classmethod
    def mutate(cls, root, info, input, id):
        delivery = Delivery.objects.get(pk=id)
        delivery.price = input.price
        delivery.type = input.type
        delivery.time = input.time
        delivery.priority = input.priority
        delivery.save()
        return UpdateDelivery(delivery=delivery)


class ClientInput(graphene.InputObjectType):
    first_name = graphene.String()
    surname = graphene.String()
    birthdate = graphene.Date()
    address = graphene.String()
    phone_number = graphene.String()
    bank_account = graphene.String()
    email = graphene.String()
    password = graphene.String()


class CreateClient(graphene.Mutation):
    class Arguments:
        input = ClientInput(required=True)

    client = graphene.Field(ClientType)

    @classmethod
    def mutate(cls, root, info, input):
        client = Client()
        client.first_name = input.first_name
        client.surname = input.surname
        client.address = input.address
        client.birthdate = input.birthdate
        client.phone_number = input.phone_number
        client.bank_account = input.bank_account
        client.email = input.email
        client.password = input.password
        client.save()
        return CreateClient(client=client)


class UpdateClient(graphene.Mutation):
    class Arguments:
        input = ClientInput(required=True)
        id = graphene.ID()

    client = graphene.Field(ClientType)

    @classmethod
    def mutate(cls, root, info, input, id):
        client = Client.objects.get(pk=id)
        client.first_name = input.first_name
        client.surname = input.surname
        client.address = input.address
        client.birthdate = input.birthdate
        client.phone_number = input.phone_number
        client.bank_account = input.bank_account
        client.email = input.email
        client.password = input.password
        client.save()
        return UpdateClient(client=client)


class OrderInput(graphene.InputObjectType):
    client = graphene.String()
    delivery = graphene.String()
    quantity = graphene.String()
    price = graphene.String()
    address = graphene.String()
    phone = graphene.String()
    date = graphene.Date()
    status = graphene.String()


class CreateOrder(graphene.Mutation):
    class Arguments:
        input = OrderInput(required=True)

    order = graphene.Field(OrderType)

    @classmethod
    def mutate(cls, root, info, input):
        order = Order()
        order.client = input.client
        order.delivery = input.delivery
        order.quantity = input.quantity
        order.price = input.price
        order.address = input.address
        order.phone = input.phone
        order.date = input.date
        order.status = input.status
        order.save()
        return CreateOrder(order=order)


class UpdateOrder(graphene.Mutation):
    class Arguments:
        input = OrderInput(required=True)
        id = graphene.ID()

    order = graphene.Field(OrderType)

    @classmethod
    def mutate(cls, root, info, input, id):
        order = Order.objects.get(pk=id)
        order.client = input.client
        order.delivery = input.delivery
        order.quantity = input.quantity
        order.price = input.price
        order.address = input.address
        order.phone = input.phone
        order.date = input.date
        order.status = input.status
        order.save()
        return UpdateOrder(order=order)


class ReviewInput(graphene.InputObjectType):
    book = graphene.String()
    client = graphene.String()
    scale_points = graphene.String()
    read_date = graphene.Date()
    advantages = graphene.String()
    disadvantages = graphene.String()
    recommend = graphene.Boolean()
    read_again = graphene.Boolean()


class CreateReview(graphene.Mutation):
    class Arguments:
        input = ReviewInput(required=True)

    review = graphene.Field(ReviewType)

    @classmethod
    def mutate(cls, root, info, input):
        review = Review()
        review.book = input.book
        review.client = input.client
        review.scale_points = input.scale_points
        review.read_date = input.read_date
        review.advantages = input.advantages
        review.disadvantages = input.disadvantages
        review.recommend = input.recommend
        review.read_again = input.read_again
        review.save()
        return CreateReview(review=review)


class UpdateReview(graphene.Mutation):
    class Arguments:
        input = ReviewInput(required=True)
        id = graphene.ID()

    review = graphene.Field(ReviewType)

    @classmethod
    def mutate(cls, root, info, input, id):
        review = Review.objects.get(pk=id)
        review.book = input.book
        review.client = input.client
        review.scale_points = input.scale_points
        review.read_date = input.read_date
        review.advantages = input.advantages
        review.disadvantages = input.disadvantages
        review.recommend = input.recommend
        review.read_again = input.read_again
        review.save()
        return UpdateReview(review=review)


class BookHasOrderInput(graphene.InputObjectType):
    book = graphene.String()
    order = graphene.String()


class CreateBookHasOrder(graphene.Mutation):
    class Arguments:
        input = BookHasOrderInput(required=True)

    book_has_order = graphene.Field(BookHasOrderType)

    @classmethod
    def mutate(cls, root, info, input):
        book_has_order = BookHasOrder()
        book_has_order.book = input.book
        book_has_order.order = input.order
        book_has_order.save()
        return CreateBookHasOrder(book_has_order=book_has_order)


class UpdateBookHasOrder(graphene.Mutation):
    class Arguments:
        input = BookHasOrderInput(required=True)
        id = graphene.ID()

    book_has_order = graphene.Field(BookHasOrderType)

    @classmethod
    def mutate(cls, root, info, input, id):
        book_has_order = BookHasOrder.objects.get(pk=id)
        book_has_order.book = input.book
        book_has_order.order = input.order
        book_has_order.save()
        return UpdateBookHasOrder(book_has_order=book_has_order)


class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    update_delivery = UpdateDelivery.Field()
    create_delivery = CreateDelivery.Field()
    update_client = UpdateClient.Field()
    create_client = CreateClient.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    create_review = CreateReview.Field()
    update_review = UpdateReview.Field()
    create_book_has_order = CreateBookHasOrder.Field()
    update_book_has_order = UpdateBookHasOrder.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

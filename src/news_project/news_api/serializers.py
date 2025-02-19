from rest_framework import serializers
from news.models import Article, ArticleImage, Category, FavoriteArticle

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model =ArticleImage
        fields = ('id', 'image', 'uploaded_at')

class FavoriteArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteArticle
        fields = ('user', 'article')

class ArticleSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    images = ArticleImageSerializer(many=True, read_only=True)
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'author', 'categories', 'images', 'is_favorite' )

    def get_is_favorite(self, article):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return FavoriteArticle.objects.filter(user=request.user, article=article).exists()
        return False

class ArticleCreationSerializer(serializers.ModelSerializer):

    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all(), required=False)
    images = serializers.ListField(
        child= serializers.FileField(max_length=100000, allow_empty_file=False),
        required=False,
        write_only=True
    )

    class Meta:
        model = Article
        fields = ('title', 'content','categories', 'images')

    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])
        images_data = validated_data.pop('images', [])
        article = Article.objects.create(**validated_data)

        if categories_data:
            article.categories.set(categories_data)

        for image in images_data:
            ArticleImage.objects.create(article=article, image=image)

        return article


from rest_framework import serializers
from .models import Article, Category, ArticleImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ('images', 'uploaded_at')


class ArticleSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    images = ArticleImageSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('created_at', 'owner', 'id')


class ArticleCreateSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        required=False
    )
    new_category_name = serializers.CharField(required=False, allow_blank=True)
    new_category_description = serializers.CharField(required=False, allow_blank=True)
    images = serializers.ListField(
        child=serializers.FileField(allow_empty_file=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = Article
        fields = [
            'title', 'content', 'categories',
            'new_category_name', 'new_category_description', 'images'
        ]

    def create(self, validated_data):

        categories = validated_data.pop('categories', [])
        new_category_name = validated_data.pop('new_category_name', None)
        new_category_description = validated_data.pop('new_category_description', None)
        images = validated_data.pop('images', [])

        article = Article.objects.create(**validated_data)

        if categories:
            article.categories.set(categories)

        if new_category_name:
            category, _ = Category.objects.get_or_create(
                name=new_category_name,
                defaults={'description': new_category_description}
            )
            article.categories.add(category)

        for image in images:
            ArticleImage.objects.create(article=article, images=image)

        return article

    def update(self, article, validated_data):
        categories = validated_data.pop('categories', [])

        for attr, value in validated_data.items():
            setattr(article, attr, value)
        article.save()

        article.categories.set(categories)

        return article

from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import (
    AbstractUser,
    PermissionsMixin,
    UserManager,
)

# Create your models here.
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models import BaseModel

phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message=(
        "Les numéros de téléphones doivent être renseignés avec le format :"
        "'+999999999'. jusqu'à 15 chiffres sont autorisés"
    ),
)


# Create your models here.
class Organism(BaseModel):
    """Organisms model"""

    uuid = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        verbose_name=_("Identifiant unique"),
    )
    label = models.CharField(
        max_length=500, unique=True, verbose_name=_("Nom")
    )
    short_label = models.CharField(
        max_length=50, unique=True, verbose_name=_("Nom court")
    )
    email = models.EmailField(
        blank=True, null=True, verbose_name=_("Adresse mail")
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        verbose_name=_("Numéro de téléphone"),
    )
    url = models.URLField(
        max_length=200, blank=True, null=True, verbose_name=_("URL")
    )
    extra_data = models.JSONField(
        blank=True, null=True, verbose_name=_("Additional datas")
    )
    logo = models.ImageField(_("Logo"), upload_to=settings.MEDIA_UPLOAD)

    class Meta:
        verbose_name_plural = _("organismes")

    def __str__(self):
        return self.short_label


class User(BaseModel, AbstractUser, PermissionsMixin):
    """Custom app user model"""

    uuid = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        verbose_name=_("Identifiant unique"),
    )
    phone = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_("Numéro de téléphone fixe"),
    )
    address = models.TextField(_("Address"), blank=True, null=True)
    comment = models.TextField(
        blank=True, null=True, verbose_name=_("Commentaire")
    )
    extra_data = models.JSONField(blank=True, null=True)
    default_area = models.ForeignKey(
        "geo_area.GeoArea",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Emprise géographique par défaut"),
    )
    organism = models.ForeignKey(
        "Organism",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Organisme"),
    )
    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f"{self.username} <{self.email}>"

    def save(self, *args, **kwargs):
        # self.username = generate_username(self.first_name, self.last_name)
        self.last_name = self.last_name.upper()
        super(User, self).save(*args, **kwargs)

    def full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

from django.urls import path
from .views import HealthCheckView, RandomBitView, CoinFlipView, RandomNumberView

urlpatterns = [
    path(
        "health/",
        HealthCheckView.as_view(),
        name="health-check"
    ),
    path(
        "quantum/random-bit/",
        RandomBitView.as_view(),
        name="random-bit"
    ),
    path(
        "quantum/coin-flip/",
        CoinFlipView.as_view(),
        name="coin-flip"
    ),
    path(
        "quantum/random-number/",
        RandomNumberView.as_view(),
        name="random-number"
    )
]
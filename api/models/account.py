from django.db import models
from django.contrib.auth import get_user_model

class Account(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  amount = models.DecimalField(max_digits=19, decimal_places=2)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def _str_(self):
    return f"{self.name}: ${self.amount}"

  def as_dict(self):
    """Returns dictionary of Account models"""
    return {
        'id': self.id,
        'name': self.name,
        'type': self.type,
        'amount': self.amount
    }



#

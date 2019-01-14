from django.db import models

# 名人名言
class Quote(models.Model):
    """
    The scrapped data will be saved in this model
    """
   
    class Meta: 
              verbose_name='名人名言'              # 单数形式 
              verbose_name_plural='名人名言'   # 这个是复数形式

    text = models.TextField(verbose_name='名言',) # 名言
    author = models.CharField(verbose_name='作者', max_length=512) # 作者

from django.db import models

# Create your models here.
class Host(models.Model):
    hostname = models.CharField(max_length=128,unique=True) #hostname必须是唯一的
    key = models.TextField() #使用密钥连接
    os_type_choices = (('redhat','Redhat\CentOS'),
                       ('ubunut','Ubuntu'),
                       ('suse','Suse'),
                       ('windows','Windows'))

    os_type = models.CharField(choices=os_type_choices,max_length=64,default='redhat')
    status_choices = ((0,'Waitting Approval'),
                      (1,'Accepted'),
                      (2,'Rejected'),)
    status = models.SmallIntegerField(choices=status_choices,default=0) #默认为0等待审核

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = u'主机'
        verbose_name_plural = verbose_name


class HostGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)
    hosts = models.ManyToManyField(Host,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '主机组'
        verbose_name_plural = verbose_name
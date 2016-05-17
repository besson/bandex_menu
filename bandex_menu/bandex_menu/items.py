# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class Menu(Item):
    nome_restaurante = Field()
    status_restaurante = Field()
    data = Field()
    periodo = Field()
    pratos_principais = Field()
    guarnicoes = Field()
    sobremesa = Field
    valor_calorico = Field()

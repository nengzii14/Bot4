# -*- coding: utf-8 -*-
class LineCallback(object):

    def __init__(self, callback):
        self.callback = callback

    def Pinverified(self, pin):
        self.callback("Masukkan Kode Pin '" + pin + "' Di Handphone anda dalam 2 menit")

    def QrUrl(self, url):
        self.callback("Cepet login anjg :( eta teh cuman 2 menit weh :( \n" + url)

    def default(self, str):
        self.callback(str)

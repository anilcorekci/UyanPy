#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# vim: ts=4:sw=4
from gi.repository import Gtk as gtk
import os

class uyan():
    total = None
    vol = 20
    def __init__(self):

		self.build = gtk.Builder()
		self.build.add_from_file("./uyan.glade")
		self.pen = self.build.get_object("window1")
		self.pen.connect("delete-event",gtk.main_quit)
		self.btn_ok = self.build.get_object("button1")
		self.btn_ono = self.build.get_object("button2")
		
		self.btn_ok.connect("clicked",self.ok)
		self.btn_ono.connect("clicked",  gtk.main_quit)
		
		self.vol = self.build.get_object("volumebutton1")
		self.vol.connect("value-changed",self.volchange)
		self.filecho = self.build.get_object("filechooserbutton1")
		
		self.scaleS =  self.build.get_object("scale1")
		self.scaleS.connect("value-changed",self.change_val)
		
		self.scaleD  = self.build.get_object("scale2")
		self.scaleD.connect("value-changed",self.change_val)
		self.pen.show_all()

    def volchange(self,widget,value):
        self.val = int( value * 100 )
        
    def ok( self,  data ):

        if self.total:
            fname = self.filecho.get_filename()
            print "Toplam Dakika: " ,  self.total
            print "Ses Seviyesi: " , self.val
            print "Çalmak içi Seçilen Dosya: " , fname
            os.system("gksudo ./spsnd_try " + str(self.total) +" " +\
                str(self.val)+ "  " +"'" +self.filecho.get_filename()+"'" + "&" )
        gtk.main_quit()            
    def change_val(self,data):
        self.total = 0
        saat = int(self.scaleS.get_value() )
        dakika = int(self.scaleD.get_value())

        
        if saat != 0:
            print "Saat  :  %s "  % ( saat )
            self.total += saat*60       
        if dakika != 0:
            print "Dakika : %s"  % ( dakika )
            self.total += dakika
        
        print "Toplam Dakika   :  %s " %( self.total)
        self.build.get_object("label4").set_text(str(self.total))        
        
        

uyan()
gtk.main()


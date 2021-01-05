# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)
import urllib
import urllib.request
from bs4 import BeautifulSoup
import datetime
import time

from string import ascii_lowercase
import string
import random
import argparse
import os
import sys

from urllib.request import urlopen, Request
import requests
import json

REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

class pcm(http.Controller):
# To render the webpage dynamically
	@http.route('/pcm/products/<int:_id>', auth='public', website=True)
	def dynamic_item_id(self, _id='', **kw):
		productcategory = http.request.env['product.category']
		#subhye=[]
		# for hyes in productcategory:
		# 	hye = {'complte_name':hyes.complete_name,}
		# 	subhye.append(hye)
		status = True
		items3=productcategory.search([('parent_id','=',False)])
		#items4 = http.request.env['ir.attachment'].search([('res_id','=', _id)])
		#_logger.error("%s" % (items3))
		subitems=[]
		for item in items3:
			val={'id':item.id,'name':item.name,'complete_name':item.complete_name,'selected':item.id, 'parent_path':item.parent_path, }
			val['subitems2'] = self.get_subitems(item.id)
			subitems.append(val)
			#_logger.error("subitems[%s]" % (subitems))
		return http.request.render('product_shelf.new_one', {
			'root': '/',
			'id':_id,
			'ProductCategory': http.request.env['product.category'].search([]),
			'item': http.request.env['product.template'].search([('categ_id', '=', _id)]),
			'productcategory': items3,
			'subitems':subitems,
			'status':status,
			'lyes': http.request.env['product.category'].search([('id', '=', _id)]),
			})

	def get_subitems(self, parentId):
		productcategory = http.request.env['product.category']
		items3=productcategory.search([('parent_id','=',parentId)])
		subitems=[]
		for item in items3:
			#_logger.error("get_subitems111111111111["+str(item)+"]")
			if productcategory.search([('parent_id','=',item.id)]):
				val={'id':item.id,'name':item.name,'complete_name':item.complete_name, 'parent_path':item.parent_path,}
				val['subitems2'] = self.get_subitems(item.id)
				subitems.append(val)
			else:
				val={'id':item.id,'name':item.name,'complete_name':item.complete_name, 'parent_path':item.parent_path,}
				val['subitems2'] = []
				subitems.append(val)
		return subitems
	#Update the database once drag and drop is accomplished
	@http.route('/pcm/update/<string:product_id>/<int:cat_id>', type='http', auth='public', website=True)
	def update_dynamic_id(self, product_id='', cat_id='', **kw):
		product_ids=product_id[:-1]
		product_ids=product_ids.split(';')
		for product_id in product_ids:
			product_id = product_ids
			values = {'categ_id':cat_id}
			product = http.request.env['product.template'].search([('id','=',product_id)])
			product.write(values)

		productcategory = http.request.env['product.category']
		items3=productcategory.search([('parent_id','=',False)])
		subitems=[]
		for item in items3:
			val={'id':item.id,'name':item.name,'complete_name':item.complete_name,'selected':item.id}
			val['subitems2'] = self.get_subitems(item.id)
			subitems.append(val)
		return http.request.render('product_shelf.new_one', {
			'root': '/',
			'id':cat_id,
			'ProductCategory': http.request.env['product.category'].search([]),
			'item': http.request.env['product.template'].search([('categ_id', '=', cat_id)]),
			'productcategory': items3,
			'subitems':subitems
			})

	@http.route('/pcm/products/browse/<int:prod_id>', type='json', auth='public', website=True)
	def my_world(self, prod_id, **kw):
		header = {
			'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
		pools = http.request.env['product.template'].search([("id", "=", prod_id)])
		subpool = []
		#if man_code:
		for pool in pools:
			vall = {'id':pool.id, 'man_code1':pool.vendor_id, 'name':pool.name}
			#vall['julus'] = self.get_ids(pool.name)
			subpool.append(vall)
			name = pool.name
			man_code = pool.vendor_id.replace(" ", "")
			#self.flickr_scraper(man_code, prod_id, name)
			_logger.info("The values posted from man_code1111: %s" %man_code)
			self.get_images_new(man_code, prod_id, name, header)
		# return http.request.render('product_shelf.my_world',{
		# 	'root': '/',
		# 	'id': prod_id,
		# 	'values': pools,
		# 	'subpool': subpool
		#})
		result = {
					'status':'OK',
					'message':'',
		}
		return (json.dumps(result))
		
	
	def get_images_new(self,man_code, prod_id, name, header, **kw):
		i=1
		url = "https://www.google.com.au/search?q=%s&source=lnms&tbm=isch" % man_code
		_logger.info("Subitemsyyyyyyyyyyyyyy: %s" %url)
		response = urlopen(Request(url, headers={
			'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}))
		html = response.read().decode('utf-8')
		soup = BeautifulSoup(html, "html.parser")
		image_elements = soup.find_all("img", {"class": "rg_i Q4LuWd"})
		for img in image_elements:
			#temp1 = img.get('src')
			#_logger.info("11111[%s]" % (temp1))
			temp = img.get('data-src')
			if temp and i < 7:
				image = temp
				#_logger.error("11111[%s]" % (image))
				filename = str(i)
				if filename:
					path = "/usr/lib/python3/dist-packages/odoo/addons/product_shelf/static/src/img/" + str(prod_id)
					if not os.path.exists(path):
						os.mkdir(path)
					_logger.error("ath.existath.existath.exist[%s]" % (image))
					imagefile = open(path + "/" + filename + ".png", 'wb+')
					req = Request(image, headers=REQUEST_HEADER)
					resp = urlopen(req)
					imagefile.write(resp.read())
					imagefile.close()
				i += 1

	@http.route('/pcm/update/images/<int:idy>', type='json', website=True)
	def signup(self, idy, f_names, **kw):
		#try:
		#_logger.info('Filenames0000000000000 %s',kw)
		#f_names = kw.get('textBox1')
		#src_f = kw.get('id')
		src_f = idy
		#_logger.info('Filenames11111111111 %s', f_names)
		#_logger.info('Filenames1111111111122222222222222 %s', src_f)
		f_name = f_names[:-1]
		f_name = f_name.split(';')
		for f in f_name:
			_logger.info('Filenames3333333333333 %s',f)
			new_filename = self.get_rand_filename()
			#data = self.get_rand_filename()
			data = new_filename[:2]
			new_path = "//var/lib/odoo/.local/share/Odoo/filestore/iiv/"+data
			src_path = "/usr/lib/python3/dist-packages/odoo/addons/product_shelf/static/src/img/" + str(src_f) + "/" +str(f) + ".png"
			#image_src = open()
			if not os.path.exists(new_path):
				os.mkdir(new_path)
			new_file = open(new_path + "/" + new_filename , 'wb+')
			with open(src_path, 'rb') as p:
				image_src = p.read()
			new_file.write(image_src)
			new_file.close()
			fields = http.request.env.cr.execute("SELECT * FROM ir_attachment WHERE name='image_1920' AND res_model='product.template' AND res_id='"+str(src_f)+"'")
			fields1 = http.request.env['ir.attachment']
			if fields is None:
				http.request.env.cr.execute("INSERT INTO ir_attachment (res_id, name, res_model, res_field, store_fname, checksum, type, file_size, mimetype, index_content, company_id) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (src_f, 'image_1920', 'product.template', 'image_1920', data + '/' +new_filename, new_filename, 'binary', 1, 'image/jpg', 'image', 2))
				http.request.env.cr.execute("INSERT INTO ir_attachment (res_id, name, res_model, res_field, store_fname, checksum, type, file_size, mimetype, index_content, company_id) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (src_f, 'image_1920', 'product.template', 'image_256', data + '/' +new_filename, new_filename, 'binary', 1, 'image/jpg', 'image', 2))
				http.request.env.cr.execute("INSERT INTO ir_attachment (res_id, name, res_model, res_field, store_fname, checksum, type, file_size, mimetype, index_content, company_id) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (src_f, 'image_1920', 'product.template', 'image_512', data + '/' +new_filename, new_filename, 'binary', 1, 'image/jpg', 'image', 2))
				http.request.env.cr.execute("INSERT INTO ir_attachment (res_id, name, res_model, res_field, store_fname, checksum, type, file_size, mimetype, index_content, company_id) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (src_f, 'image_1920', 'product.template', 'image_1024', data + '/' +new_filename, new_filename, 'binary', 1, 'image/jpg', 'image', 2))
				http.request.env.cr.execute("INSERT INTO ir_attachment (res_id, name, res_model, res_field, store_fname, checksum, type, file_size, mimetype, index_content, company_id) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (src_f, 'image_1920', 'product.template', 'image_128', data + '/' +new_filename, new_filename, 'binary', 1, 'image/jpg', 'image', 2))
				status="Inserted"
			else:
				store_fname=data + '/' +new_filename
				http.request.env.cr.execute("UPDATE ir_attachment SET store_fname='"+ str(store_fname) +"',  checksum='"+str(new_filename)+"', company_id=2 WHERE res_id='"+str(src_f)+"'")
				status="Updated"
		#return ("Database Succesfully %s!!" % (status))
		#gauls = http.request.env['product.template'].search([("id", "=", src_f)])
		# http.request.env.cr.execute("SELECT categ_id FROM product_template WHERE id='"+str(src_f)+"'")
		# for res in http.request.env.cr.fetchall():
		# 	gauls = {'categ_id': res[0]}
		# 	_logger.info('Oeeeeyyyyyyyyyeyeyeyeyeyeeyeyey [%s]' %(gauls))
		# #_logger.info('Oeeeeyyyyyyyyyeyeyeyeyeyeeyeyey [%s]' %(gauls))
		# sugauls = []
		# insub = []
		# insub.append(gauls)
		# _logger.info('Oeeeeyyyyyyyyyeyeyeyeyeyeeyeyey111111111 [%s]' %(sugauls))
		# _logger.info('Oeeeeyyyyyyyyyeyeyeyeyeyeeyeyey111111111 [%s]' %(sugauls))
		# _logger.info('Oeeeeyyyyyyyyyeyeyeyeyeyeeyeyey111111111 %s' %insub)
		# return http.request.render('product_shelf.new_world',{
		# 	'root': '/',
		# 	'id': src_f,
		# 	'insub': insub,
		# 	'gauls': gauls
		# })
		result = {
				'status':'OK',
				'message':'Upload Accomplish',
		}
		return (json.dumps(result))
		#except:
		#	return ("Failed to Update the Database. Please redirect to erp13.bosspacific.com.au:8069/")
	def get_rand_filename(self):
		alf_num = 40
		checksum = ''.join(random.choices(string.ascii_lowercase + string.digits, k = alf_num))
		return checksum
	
	@http.route('/pcm/category/<int:idx>', type='json', auth='public', website=True)
	def create_category(self, idx, name, complete_name, parent_path, **kw):
		#prod_cat = http.request.env['product.category'].search([('id', '=', idx)])
		#kittens = http.request.env['product.category'].search([])
		#http.request.env.cr.execute("SELECT id FROM product_category ORDER BY id DESC LIMIT 1")
		#alfa = http.request.env.cr.fetchone()
		beta = http.request.env['product.category'].search([], order='id desc')[0].id
		beta = int(beta) + 1
		#_logger.info("wwwwwwwwwwwwwwwwwwwwwwwww[%s]" % (alfa))
		_logger.info("wwwwwwwwwwwwwwwwwwwwwwwww[%s]" % (beta))
		#_logger.info("xxxxxxxxxxxxxxxxxxxxxxxx[%s]" % (kw))
		#base = []
		#base.append(kw)
		#name = kw.get('name')
		#_logger.info("xxxxxxxxxxxxxxxxxxxxxxxx[%s]" % (name))
		#complete_name = kw.get('complete_name') + ' / ' + str(name)
		#_logger.info("xxxxxxxxxxxxxxxxxxxxxxxx[%s]" % (complete_name))
		#parent_path = parent_path + '/' + str(beta)
		if len(parent_path) > 1:
			parent_path = parent_path +  str(beta)
		else:
			parent_path = parent_path
		_logger.info("Dil kyu yeh mera sor kare[%s]" % (parent_path))

		if len(parent_path) > 1:
			parent_id = int(parent_path.split("/")[-2])
		else:
			parent_id = int(parent_path)
		_logger.info("xxxxxxxxxxxxxxxxxxxxxxxx[%s]" % (parent_id))

		#noob = {'parent_id':parent_id}
		#base.append(noob)
		#_logger.info("xxxxxxxxxxxxxxxxxxxxxxxx[%s]" % (base))
		base = {'id': beta, 'parent_path': str(parent_path), 'name': str(name),  'complete_name': str(complete_name), 'parent_id': parent_id}
		_logger.info("basesesesesesesessesese[%s]" % (base))
		#kittens.create(base)
		http.request.env.cr.execute("INSERT INTO product_category (id, parent_path, name, complete_name, parent_id) VALUES ('%s', '%s', '%s', '%s', '%s')" % (beta, parent_path, name, complete_name, parent_id))
		#for cat in prod_cat:
		# 	my_tuple={'id'}
		# prod_cat.create(my_tuple)
		#return http.request.render('product_shelf.old_world',{
		#	'root': '/',
		#	'id': idx,
		#	'prod_cat': prod_cat,
		#})
		result = {
				'status': 'OK',
				'message': '',
				'idi': beta,
		}
		return (json.dumps(result))

	@http.route('/pcm/delete/<int:idw>', type='json', auth='public', website=True)
	def delete_category(self, idw, **kw):
		#error handling to check the foreign key constraint violation
		http.request.env.cr.execute("SELECT id FROM product_template WHERE categ_id="+str(idw)+"") 
		#gun =http.request.env.cr.execute("SELECT id  from product_category WHERE parent_id ="+str(idw)+"")
		#sun = http.request.env['product.category'].search([('parent_id', '=', idw)])
		#this value also needs to be appended to the list for a fail-proof system that handles all the exceptions
		#http.request.env.cr.execute("SELECT id  from product_category WHERE parent_id ="+str(idw)+"")
		naja = http.request.env.cr.fetchall()
		#naja = http.request.env['product.template'].search([('categ_id', '=', idw)])
		val = []
		sol = self._get_parent_id(idw=idw)
		for item in naja:
			#book = item.id
			book = item
			val.append(book)
		_logger.info("All the world's a stage and all the men and women merely players %s " % (val))
		# for dor in sun:
		# 	#dor = sun.id
		# 	sol.append(dor.id)
		# _logger.info("A journey of a thousand mile begins with a single step %s " % (sol))
		if len(val) > 0:
			#http.request.env.cr.execute("DELETE FROM product_category WHERE id="+str(idw)+"")
			result = {
				'status': '!OKEY',
				'message': '',
				'zoop': len(val),
			}
		elif len(sol) > 0:
			result = {
				'status': '!OKEY',
				'message': '',
			}
		else:
			http.request.env.cr.execute("DELETE FROM product_category WHERE id="+str(idw)+"")
			result = {
				'status': 'OK',
				'message': '',
			}

		return (json.dumps(result))

	def _get_parent_id (self,idw, **kw):
		sun = http.request.env['product.category'].search([('parent_id', '=', idw)])
		sol1=[]
		for dor in sun:
			#dor = sun.id
			sol1.append(dor.id)
		return sol1

	@http.route('/pcm/prodel/<int:idk>', type='json', auth='public', website=True)
	def al_del_prod (self, idk, **kw):
		#http.request.env.cr.execute("DELETE FROM product_template WHERE categ_id="+str(idk)+"")
		wir =  http.request.env['product.template'].search([('categ_id', '=', idk)])
		tore = self.search_child(idk)
		wire =  []
		#res = []
		for i in wir:
			wire.append(i)
		_logger.info("Marhaba Ya Mustafa, Marhaba Ya Mustafa, Marhaba Ya Mustafa %s " % (wire))
		zoop = str(len(wire))
		_logger.info("Khwajamrerekhwajadilmeinsamajashahokashahtualikadulara %s " % (zoop))
		if len(wire)>0:
			self.drop_prod(idk)
			self.al_cat_del(idk)
			result = {
				'status': 'tamam',
				'message': '',
				#'zoop': zoop,
			}

		elif len(tore) > 0:
			result = {
				'status': '!OKEY',
				'message': '',
				#'zoop': zoop,
			}

		else: 
			result = {
					'status': 'OK',
					'message': '',
					#'zoop': '0',
			}
		_logger.info("Sa Re Ga Ma Pa Dha Ni Sa %s " % (result))
		return (json.dumps(result))

	def drop_prod(self, cid, **kw):
		http.request.env.cr.execute("DELETE FROM product_template WHERE categ_id="+str(cid)+"")

	def al_cat_del(self, catid, **kw):
		http.request.env.cr.execute("DELETE FROM product_category WHERE id="+str(catid)+"")

	def search_child(self, lid, **kw):
		tor = http.request.env['product.category'].search([('parent_id', '=', lid)])
		res = []
		for him in tor:
			res.append(him)
		return res
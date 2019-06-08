import webbrowser
import shutil
import glob
import os
import time

year, month, day = time.strftime("%y,%m,%d").split(',')
today_date = year + month + day

def launch_banks():
	url_ih = "https://www.devenir-rentier.fr/profile.php?section=tools&id=9897"
	url_lbp = "https://www.labanquepostale.fr/"
	url_hdf = "https://netbanking.hdfcbank.com/netbanking/"
	url_for = "https://mabanque.fortuneo.fr/fr/prive/default.jsp?ANav=1"

	chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
	webbrowser.get(chrome_path).open_new(url_ih)
	webbrowser.get(chrome_path).open_new(url_lbp)
	webbrowser.get(chrome_path).open_new(url_for)
	webbrowser.get(chrome_path).open_new(url_hdf)

def launch_dashboards():
	#C:\Users\Fabrice Foucaud\Google Drive\Dashboards
	#C:\Program Files (x86)\LibreOffice 5\program
	dashboards_path = "C:/Users/Fabrice Foucaud/Google Drive/Dashboards"
	os.chdir(dashboards_path)
	list_of_dashboards = glob.glob('*')
	src_dashboards = max(list_of_dashboards, key=os.path.getctime)
	dst_dashboards = today_date + "-Dashboards.ods"
	dst_dashboards_path = dashboards_path + "/" + dst_dashboards
	print("Copy " + src_dashboards + " to " + dst_dashboards)
	shutil.copyfile(src_dashboards,dst_dashboards)
	scalc_path = "C:\Program Files (x86)\LibreOffice 5\program"
	cmd_dash = 'start "'+scalc_path+"\soffice.bin"+'" '+dst_dashboards + " &"
	print(cmd_dash)
	os.system(cmd_dash)

def launch_xlsportfolio():
	#C:\Users\Fabrice Foucaud\Google Drive\xlsPorfolio
	#C:\Program Files (x86)\Microsoft Office\Office12
	xls_path = "C:/Users/Fabrice Foucaud/Google Drive/xlsPorfolio"
	os.chdir(xls_path)
	list_of_xls = glob.glob('*')
	src_xls = max(list_of_xls, key=os.path.getctime)
	dst_xls = today_date + "-XlsPortfolio.xls"
	print("Copy " + src_xls + " to " + dst_xls)
	shutil.copyfile(src_xls,dst_xls)	
	excel_path = "C:\Program Files (x86)\Microsoft Office\Office12"
	cmd_dash = 'start "'+excel_path+"\EXCEL.exe"+'" '+dst_xls + " &"
	print(cmd_dash)
	os.system(cmd_dash)	

launch_dashboards()
launch_xlsportfolio()
launch_banks()
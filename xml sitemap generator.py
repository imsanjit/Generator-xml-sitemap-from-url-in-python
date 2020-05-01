#@title Generator xml sitemap from multiple urls { vertical-output: true, form-width: "50%", display-mode: "form" }

changefreq = "daily" #@param ["daily", "weekly", "monthly"]
lastmod_date = "2020-04-30" #@param {type:"date"}
priority = 0.8 #@param {type:"slider", min:0, max:1, step:0.1}
#@markdown After choosing your options run the program by pressing the play button. 
#@markdown After that paste your urls in given box..

import xml.etree.cElementTree as ET
from lxml import etree
import datetime
from google.colab import files
#@markdown Note: Urls should be in a single line...
input_urls = input("Enter your urls here: \n\n").split(sep=' ')

urlset = ET.Element("urlset", xmlns="http:www.sitemaps.org/schemas/sitemap/0.9")

for x_url in input_urls:
    doc = ET.SubElement(urlset, "url")
    ET.SubElement(doc, "loc").text = str(x_url)
    ET.SubElement(doc, "lastmod").text = lastmod_date
    ET.SubElement(doc, "changefreq").text = changefreq
    ET.SubElement(doc, "priority").text = str(priority)
    tree = ET.ElementTree(urlset)
tree.write("sitemap.xml")

print(f"\n Sitemap is Ready....")

try:
  files.download("sitemap.xml")
  print(f'\nAll Done \nFile Downloaded with file name "{output_file}"')
except:
  print(f'\nIf your file is not downloaded, Kindly Download your file from left nav folder. File name is "sitemap.xml"')

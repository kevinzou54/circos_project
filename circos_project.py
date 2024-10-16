from flask import Flask, render_template, request, redirect, url_for
import subprocess, os
from subprocess import Popen
from logging import FileHandler,WARNING

app = Flask(__name__, static_folder='/home/kevin/Desktop/circos-0.69-9/Test/PlotPlot')

file_handler = FileHandler("errorlog.txt")
file_handler.setLevel(WARNING)

@app.route("/", methods=['GET','POST'])
def hello():
	if request.method=='POST':
		radius = request.form['radius']
		link_data = request.form['links']
		chromosomes = request.form['chromosomes']
		link_radius = request.form['link_radius']

		link_file = open('/home/kevin/Desktop/circos-0.69-9/Test/PlotPlot/data/kevins_links_2.txt', 'w')
		link_file.flush()
		link_file.write(link_data)
		link_file.close()
	

		with open('/home/kevin/Desktop/circos-0.69-9/Test/PlotPlot/etc/circos.conf', 'r') as file:
			chr_file_data = file.readlines()
		
		file.close()
		if(chromosomes==" "):
			chrom_input = "chromosomes=/hs.*$/\n"
		else:
			chrom_input = "chromosomes=" + chromosomes + "\n"
					
		if(link_radius == ""):
			link_rad_input = "radius = 0.9r\n"
		else:
			link_rad_input = "radius = " + link_radius + "r\n"
		chrom_search = "chromosomes="
		link_rad_search = "radius = "
		new_file_data = list()

		for i in chr_file_data:
			if chrom_search in i:
				new_file_data.append(chrom_input)
			elif link_rad_search in i:
				new_file_data.append(link_rad_input)
			else:
				new_file_data.append(i)

		
		with open('/home/kevin/Desktop/circos-0.69-9/Test/PlotPlot/etc/circos.conf', 'w') as file:
        		file.writelines(new_file_data)
		file.close()



		with open('/home/kevin/Desktop/circos-0.69-9/Test/PlotPlot/etc/ideogram.position.conf', 'r') as file:
			data = file.readlines()
			print(data)			
		data[0] = "radius = " + radius + "r\n"
		with open('/home/kevin/Desktop/circos-0.69-9/Test/PlotPlot/etc/ideogram.position.conf', 'w') as file:
			file.writelines(data)
		file.close()

		with open('/home/kevin/Desktop/circos-0.69-9/Test/PlotPlot/etc/ideogram.conf', 'r') as file:
			band_file_data = file.readlines()
		file.close()
		new_file_data = list()
		band_search = "show_bands"
		
		if(request.form.get('bands')):
			band_input = "show_bands = yes\n"
		else:
			band_input = "show_bands = no\n"

		for line in band_file_data:
			if band_search in line:
				new_file_data.append(band_input)
			else:
				new_file_data.append(line)
		with open('/home/kevin/Desktop/circos-0.69-9/Test/PlotPlot/etc/ideogram.conf', 'w') as file:
			file.writelines(new_file_data)
		file.close()

				

		os.chdir("/home/kevin/Desktop/circos-0.69-9/Test/PlotPlot")
		my_env = os.environ.copy()
		my_env["PATH"] = "/usr/bin"
		p = subprocess.run("../../bin/circos -conf etc/circos.conf -debug_group summary,timer > run.out", shell = True, cwd = "/home/kevin/Desktop/circos-0.69-9/Test/PlotPlot", capture_output=True, env=my_env)
		print("hello")
		return redirect(url_for('displayImg'))
	
	
	return render_template('createPlot.html')

@app.route('/displayImg', methods=['GET', 'POST'])
def displayImg():
	if request.method=='POST':
		return redirect(url_for('hello'))
	return render_template("displayImage.html")

	


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

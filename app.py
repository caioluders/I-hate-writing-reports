import dearpygui.dearpygui as dpg

def clear_intro() :
	dpg.delete_item("open_btn")
	dpg.delete_item("newr_btn")
	dpg.delete_item("newt_btn")

def insert_texts() :
		with dpg.table(id="main_table",parent="main_window",policy=dpg.mvTable_SizingStretchProp ,header_row=False,borders_innerH=False,borders_outerH=False, borders_innerV=False, borders_outerV=False) :
			dpg.add_table_column()
			dpg.add_table_column()

			with dpg.table_row():
				dpg.add_input_text(multiline=True,width=dpg.get_viewport_client_width(),height=dpg.get_viewport_height(),  tab_input=True, id="report_text_md")
			with dpg.table_row() :
				dpg.add_text("Render PDF")

def open_btn_callback(sender, app_data, user_data):
	print("Sender:", sender) 
	print("App data:", app_data)

	file_name = app_data["selections"][list(app_data["selections"].keys())[0]]

	clear_intro()
	insert_texts()
	report_text = open(file_name,'r').read()
	dpg.set_value("report_text_md",report_text)
	
def newr_btn_callback():
	print("new report pressed") 

def newt_btn_callback():
	print("new template pressed") 

with dpg.file_dialog(directory_selector=False, show=False, callback=open_btn_callback, id="file_dialog_id"):
    dpg.add_file_extension(".*", color=(255, 255, 255, 255))

with dpg.window(label="I Hate Writing Reports", autosize=True, id="main_window"):
	dpg.add_text("I Hate Writing Reports")
	dpg.add_button(label="Open" , callback=lambda: dpg.show_item("file_dialog_id"), id = "open_btn")
	dpg.add_button(label="New Report" , callback = newr_btn_callback, id = "newr_btn")
	dpg.add_button(label="New Template", callback=newt_btn_callback ,id = "newt_btn")

dpg.set_primary_window("main_window", True)

dpg.start_dearpygui()

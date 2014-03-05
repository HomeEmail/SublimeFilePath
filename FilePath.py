import sublime, sublime_plugin, string


class SaveSessionCommand(sublime_plugin.TextCommand):
	settings = None
	init_dir=""
	def run(self, edit):
		'''
		win=sublime.active_window()
		fileName=''
		fileNameTemp=self.view.file_name()
		fileName+='filename="'+fileNameTemp+'"\r\n'
		newView=win.new_file()
		newView.insert(edit,0,fileName)
		win.focus_view(newView)
		win.run_command('save')
		'''
		
		# Settings
		#self.settings = sublime.load_settings('FileBinder.sublime-settings').get('settings')
		#self.init_dir=self.settings.get("init_directory", False)


		wins=sublime.active_window()
		fileName=''

		for winView in wins.views():
			fileNameTemp=winView.file_name()
			fileName+='filename="'+fileNameTemp+'"\r\n'

		newView=wins.new_file()
		newView.insert(edit,0,fileName)
		wins.focus_view(newView)
		wins.run_command('save',self.init_dir)
		
class OpenSessionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		wins=sublime.active_window()
		#fileName=''
		viewCur=None
		viewCur=wins.active_view()
		inden_region=viewCur.find_all('^(filename=").+(")$')
		for region_item in inden_region:
			pathStr=viewCur.substr(region_item)
			pathValue=pathStr.split('"')
			#fileName+=pathValue[1]
			wins.open_file(pathValue[1]);

		
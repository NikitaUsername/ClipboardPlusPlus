import sublime, sublime_plugin
import json


class ClipboardCopyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command('copy')
		data = self.get_data()
		self.set_data(data)
		##self.view.insert(edit, 0, data["clipboardHistory"][data["index"]]["content"])

	def get_data(self):
		path = '/home/denis/.config/sublime-text-3/Packages/ClipboardPlusPlus/hist.json'
		with open(path, 'r') as f:
		    data = json.loads(f.read())	
		    f.close()
		return data

	def set_data(self, data):
		path = '/home/denis/.config/sublime-text-3/Packages/ClipboardPlusPlus/hist.json'

		if data["index"] is not 7:
			data["index"] += 1
		else:
			data["index"] = 0

		data["clipboardHistory"][data["index"]]["content"] = sublime.get_clipboard()

		with open(path, 'w') as f:
		    f.write(json.dumps(data))
		    f.close()

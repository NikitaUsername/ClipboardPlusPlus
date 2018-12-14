import sublime, sublime_plugin


class ClipboardCopyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command('copy')
import sublime, sublime_plugin, webbrowser

# TODO: allow users to change these in options
BASE_URLS = {
  'php': 'http://php.net/',
  'js': 'https://developer.mozilla.org/en-US/search?topic=js&q=',
  'css': 'https://developer.mozilla.org/en-US/search?topic=css&q=',
  'python': '',
  'ruby': ''
}

class GetDocsCommand(sublime_plugin.TextCommand):
  """
  This will search the relevent API docs for the selection(s)
  """

  def get_selections(self):

    selections = {}

    for region in self.view.sel():
      scope_name = self.view.scope_name(region.begin()).rpartition('.')[2].strip()
      if scope_name in selections:
        selections[scope_name].append(self.view.substr(region))
      else:
        selections[scope_name] = [self.view.substr(region)]

    return selections

  def run(self, edit, language=''):
    selections = self.get_selections()

    for (scope_name, selection_list) in selections.items():

      if language != '':
        language = language
      else:
        language = scope_name

      print(language)

      for selection in selection_list:
        if (language in BASE_URLS):
          webbrowser.open_new_tab(BASE_URLS[language] + selection)
        else:
          webbrowser.open_new_tab('https://www.google.com/#q=' + selection)

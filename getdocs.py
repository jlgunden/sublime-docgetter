import sublime, sublime_plugin, webbrowser

# TODO: allow users to change these in options
BASE_URLS = {
  'PHP': 'http://php.net/',
  'JS': 'https://developer.mozilla.org/en-US/search?topic=js&q=',
  'CSS': 'https://developer.mozilla.org/en-US/search?topic=css&q=',
  'PYTHON': '',
  'RUBY': ''
}

class GetDocsCommand(sublime_plugin.TextCommand):
  """
  This will search the relevent API docs for the selection(s)
  """

  def get_selections(self):
    selections = []
    for region in self.view.sel():
      selection = self.view.substr(region)
      selections.append(selection)
    return selections

  def run(self, edit, language=''):
    selections = self.get_selections()

    # TODO: extract scope for auto detection

    for selection in selections:
      if (language in BASE_URLS):
        webbrowser.open_new_tab(BASE_URLS[language] + selection)
      else:
        webbrowser.open_new_tab('https://www.google.com/#q=' + selection)


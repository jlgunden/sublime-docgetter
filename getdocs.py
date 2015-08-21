import sublime, sublime_plugin, webbrowser

# TODO: allow users to change these in options
BASE_URLS = {
  'php': 'http://php.net/',
  'js': 'https://developer.mozilla.org/en-US/search?topic=js&q=',
  'css': 'https://developer.mozilla.org/en-US/search?topic=css&q=',
  'python': 'http://docs.python.org/3/search.html?q=',
  'ruby': 'http://ruby-doc.com/search.html?q='
}

class GetDocsCommand(sublime_plugin.TextCommand):
  """This will search the relevent documentation for the selection(s)"""

  def get_selections(self):
    """
    Returns  selections in a dictionary where each key is a scope and its value
    is a list containing all selections belonging to that scope
    """

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
        url_key = language
      else:
        url_key = scope_name

      for selection in selection_list:
        webbrowser.open_new_tab(BASE_URLS.get(url_key, 'https://www.google.com/#q=') + selection)

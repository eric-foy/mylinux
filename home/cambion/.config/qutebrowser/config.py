config.load_autoconfig(False)

c.new_instance_open_target = 'tab'
c.session.default_name = 'default_session'
c.session.lazy_restore = True
c.backend = 'webengine'
c.qt.force_software_rendering = 'none'
c.qt.low_end_device_mode = 'never'
c.auto_save.interval = 0

c.content.autoplay = False
c.content.cache.size = 1048576
c.content.cookies.accept = 'no-3rdparty'
c.content.cookies.store = False
c.content.default_encoding = 'utf-8'
c.content.desktop_capture = False
c.content.geolocation = False
c.content.headers.do_not_track = False
c.content.images = True
c.content.javascript.enabled = False
c.content.javascript.can_access_clipboard = True
c.content.javascript.modal_dialog = False
c.content.local_content_can_access_file_urls = True
c.content.local_storage = False
c.content.persistent_storage = False
c.content.plugins = False
c.content.print_element_backgrounds = False
c.content.register_protocol_handler = False
c.content.tls.certificate_errors = 'ask-block-thirdparty'
c.content.user_stylesheets = '/usr/share/qutebrowser/stylesheets/no_display.css'
c.content.mute = False
c.content.canvas_reading = False
c.content.webrtc_ip_handling_policy = 'default-public-interface-only'
c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
c.content.xss_auditing = True

c.completion.cmd_history_max_items = 100
c.completion.height = '60%'
c.completion.open_categories = ["quickmarks", "bookmarks", "history"]
c.completion.shrink = True
c.completion.scrollbar.width = 12

c.downloads.location.directory = '~/downloads/'
c.downloads.location.prompt = True
c.downloads.location.suggestion = 'path'
c.downloads.open_dispatcher = '"termite -e xdg-open {}"'
c.downloads.remove_finished = 2000

c.editor.command = ['termite', '-e', 'vim {file}']

c.hints.border = '0px solid #AD00A1'
c.hints.chars = 'aoeuidhtns'
c.hints.selectors['all'].append('d2l-dropdown')
c.hints.selectors.update({'text': ['span[class="primaryTerm"]', 'span[class="definition nb_hidden clAnnotationDecoration"]', 'span[class="term"]', 'div[class="study--concept-text-container ng-scope"']})
c.hints.uppercase = False

c.input.insert_mode.auto_enter = False
c.input.insert_mode.auto_leave = False
c.input.links_included_in_focus_chain = False
c.input.partial_timeout = 4000
c.input.spatial_navigation = False

c.keyhint.radius = 4
c.keyhint.delay = 0

c.messages.timeout = 500

c.prompt.filebrowser = True
c.prompt.radius = 0

c.spellcheck.languages = ['en-US']

c.statusbar.padding = {'top': 1, 'bottom': 1, 'left': 0, 'right': 0}
c.statusbar.widgets = ['keypress', 'url', 'scroll', 'history', 'tabs', 'progress']

c.tabs.background = False
c.tabs.favicons.show = 'never'
c.tabs.last_close = 'close'
c.tabs.mousewheel_switching = False
c.tabs.new_position.related = 'next'
c.tabs.new_position.stacking = True
c.tabs.new_position.unrelated = 'first'
c.tabs.padding = {'top': 1, 'bottom': 1, 'left': 0, 'right': 0}
c.tabs.select_on_remove = 'next'
c.tabs.show_switching_delay = 0
c.tabs.title.format = '{current_title}'
c.tabs.indicator.width = 3
c.tabs.indicator.padding = {'top': 2, 'bottom': 2, 'left': 0, 'right': 4}
c.tabs.undo_stack_size = 5

c.url.auto_search = 'naive'
c.url.default_page = 'about:blank'
c.url.open_base_url = True
c.url.searchengines = {
        'DEFAULT': 'https://en.wikipedia.org/w/index.php?search={}',
        'duck': 'https://duckduckgo.com/html/?q={}',
        'google': 'https://www.google.com/search?hl=en&q={}',
        'arch': 'https://wiki.archlinux.org/?search={}',
        'wiki': 'https://en.wikipedia.org/w/index.php?search={}',
        'aur': 'https://aur.archlinux.org/packages/?O=0&K={}',
        'pacman': 'https://www.archlinux.org/packages/?q={}',
        'git': 'https://github.com/search?q={}',
        'pirate': 'http://www.thepiratebay.org/search?q={}',
        'stack': 'https://stackexchange.com/search?q={}',
        'fdroid': 'https://search.f-droid.org/?q={}&lang=en',
}
c.url.start_pages = 'about:blank'

c.window.hide_decoration = False
c.window.title_format = '{current_url}'

base00 = "#231f20"
base01 = "#1c3f95"
base02 = "#5a5758"
base03 = "#737171"
base04 = "#959ca1"
base05 = "#d9d8d8"
base06 = "#e7e7e8"
base07 = "#ffffff"
base08 = "#ee2e24"
base09 = "#f386a1"
base0A = "#ffd204"
base0B = "#00853e"
base0C = "#85cebc"
base0D = "#009ddc"
base0E = "#98005d"
base0F = "#b06110"

c.colors.completion.fg = base05
c.colors.completion.odd.bg = base00
c.colors.completion.even.bg = base00
c.colors.completion.category.fg = base04
c.colors.completion.category.bg = base01
c.colors.completion.category.border.top = base01
c.colors.completion.category.border.bottom = base01
c.colors.completion.item.selected.fg = base00
c.colors.completion.item.selected.bg = base0A
c.colors.completion.item.selected.border.top = base0A
c.colors.completion.item.selected.border.bottom = base0A
c.colors.completion.match.fg = base0B
c.colors.completion.scrollbar.fg = base04
c.colors.completion.scrollbar.bg = base01
c.colors.downloads.bar.bg = base00
c.colors.downloads.start.fg = base00
c.colors.downloads.start.bg = base0D
c.colors.downloads.stop.fg = base00
c.colors.downloads.stop.bg = base0C
c.colors.downloads.error.fg = base08
c.colors.hints.fg = base06
c.colors.hints.bg = base0E
c.colors.hints.match.fg = base0B
c.colors.keyhint.fg = base06
c.colors.keyhint.suffix.fg = base0B
c.colors.keyhint.bg = base0E
c.colors.messages.error.fg = base05
c.colors.messages.error.bg = base08
c.colors.messages.error.border = base08
c.colors.messages.warning.fg = base00
c.colors.messages.warning.bg = base0E
c.colors.messages.warning.border = base0E
c.colors.messages.info.fg = base05
c.colors.messages.info.bg = base00
c.colors.messages.info.border = base00
c.colors.prompts.fg = base05
c.colors.prompts.border = base00
c.colors.prompts.bg = base00
c.colors.prompts.selected.bg = base0A
c.colors.statusbar.normal.fg = base0B
c.colors.statusbar.normal.bg = base00
c.colors.statusbar.insert.fg = base00
c.colors.statusbar.insert.bg = base0D
c.colors.statusbar.passthrough.fg = base00
c.colors.statusbar.passthrough.bg = base0C
c.colors.statusbar.private.fg = base00
c.colors.statusbar.private.bg = base03
c.colors.statusbar.command.fg = base05
c.colors.statusbar.command.bg = base00
c.colors.statusbar.command.private.fg = base05
c.colors.statusbar.command.private.bg = base00
c.colors.statusbar.caret.fg = base00
c.colors.statusbar.caret.bg = base0E
c.colors.statusbar.caret.selection.fg = base00
c.colors.statusbar.caret.selection.bg = base0D
c.colors.statusbar.progress.bg = base0D
c.colors.statusbar.url.fg = base05
c.colors.statusbar.url.error.fg = base08
c.colors.statusbar.url.hover.fg = base05
c.colors.statusbar.url.success.http.fg = base0C
c.colors.statusbar.url.success.https.fg = base0B
c.colors.statusbar.url.warn.fg = base0E
c.colors.tabs.bar.bg = base00
c.colors.tabs.indicator.start = base0D
c.colors.tabs.indicator.stop = base0C
c.colors.tabs.indicator.error = base08
c.colors.tabs.odd.fg = base05
c.colors.tabs.odd.bg = base01
c.colors.tabs.even.fg = base05
c.colors.tabs.even.bg = base01
c.colors.tabs.selected.odd.fg = base00
c.colors.tabs.selected.odd.bg = base0D
c.colors.tabs.selected.even.fg = base00
c.colors.tabs.selected.even.bg = base0D

#c.fonts.monospace = 'Inconsolata'
c.fonts.completion.entry = '14px Inconsolata'
c.fonts.completion.category = '14px Inconsolata'
c.fonts.debug_console = '14px Inconsolata'
c.fonts.downloads = '14px Inconsolata'
c.fonts.hints = 'bold 12px Hack'
c.fonts.keyhint = 'bold 12px Hack'
c.fonts.messages.error = '14px Inconsolata'
c.fonts.messages.info = '14px Inconsolata'
c.fonts.messages.warning = '14px Inconsolata'
c.fonts.prompts = '14px Inconsolata'
c.fonts.statusbar = '14px Inconsolata'
#c.fonts.tabs = '14px Inconsolata'
c.fonts.web.family.standard = 'DejaVu Sans'
c.fonts.web.family.fixed = 'Inconsolata'
c.fonts.web.family.serif = 'DejaVu Serif'
c.fonts.web.family.sans_serif = 'DejaVu Sans'
c.fonts.web.size.default = 14
c.fonts.web.size.default_fixed = 14
c.fonts.web.size.minimum = 8

#with config.pattern('*://*.wright.edu/*') as p:
#    c.content.javascript.enabled = True
#    c.content.local_storage = True
    
with config.pattern('https://*.wright.edu/*') as p:
    c.content.javascript.enabled = True
    c.content.local_storage = True

with config.pattern('https://*.bbcollab.com/*') as p:
    c.content.javascript.enabled = True
    c.content.local_storage = True

#c.bindings.key_mappings = {'<Ctrl+[>': '<Escape>', '<Ctrl+6>': '<Ctrl+^>', '<Ctrl+m>': '<Return>', '<Ctrl+j>': '<Return>', '<Shift+Return>': '<Return>', '<Enter>': '<Return>', '<Shift+Enter>': '<Return>', '<Ctrl+Enter>': '<Ctrl+Return>', '<Ctrl+Shift+v>': '<Shift+Ins>'}


config.bind(',f', 'set-cmd-text :fake-key -g f ; ;; set-cmd-text -s -a ; later 100 fake-key -g')
config.bind(',r', 'spawn --userscript readability')
config.bind(',p', 'spawn --userscript qute-pass --no-insert-mode')
config.bind(',o', 'set-cmd-text -s :session-load -c')
config.bind(',s', 'set-cmd-text -s :session-save -o')

config.bind('yh', 'yank inline {url:host}')

config.bind('pk', 'fake-key {clipboard}')

config.bind('wg', 'set-cmd-text -s :tab-give')
config.bind('wt', 'set-cmd-text -s :tab-take')

config.bind('Sk', 'open qute://bindings/')
config.bind('St', 'open qute://tabs/')
config.bind('Sl', 'open qute://log/')

config.bind('<Ctrl+w>', 'rl-unix-filename-rubout', mode='prompt')

config.bind('<Ctrl+Shift-V>', 'insert-text {primary}', mode='insert')
config.bind('<Ctrl-v>', 'set-cmd-text -a {clipboard}', mode='command')
config.bind('<Ctrl-Shift-v>', 'set-cmd-text -a {primary}', mode='command')

config.bind('cj', 'set --temp --pattern={url:domain}/* content.javascript.enabled true ;; reload')
config.bind('chs', 'set --temp --pattern={url:domain}/* content.local_storage true ;; reload')

config.bind('ab', 'hint -r links run bookmark-add {hint-url} {hint-url}')

config.bind('su', 'spawn --userscript append-to /tmp/urls');

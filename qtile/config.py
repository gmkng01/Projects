import os
import subprocess
from libqtile import hook
from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from colors import gruvbox
from mybar import mera_bar
from mybar2 import mera_bar1
from keybindings import my_keys

mod = "mod4"
mod1 = "mod1"
terminal = "terminator"
keys = my_keys


# Grouping I created -*-

# groups = [Group(i) for i in "123456789"]
groups = [
    Group('1', label="HTTPS://", matches = [Match(wm_class = "firefox")], layout='monadtall'),
    Group('2', label="CODE", matches = [Match(wm_class = "Code")], layout='max'),
    Group('3', label="TERM", layout='monadtall'),
    Group('4', label="FILE", matches = [Match(wm_class = "pcmanfm")], layout='monadtall'),
    Group('5', label="SOCIEL", matches = [Match(wm_class = "discord"), Match(wm_class="TelegramDesktop")], layout='monadtall'),
    Group('6', label="ENTER", matches = [Match(wm_class = "vysor")], layout='monlladta'),
    # Group('7', label="", layout='monadtall'),
    # Group('8', label="", layout='monadtall'),
    # Group('9', label="", layout='monadtall'),
    # Group('0', label="", layout='monadtall')
    ]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {"border_width": 0,
                "margin": 0,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.RatioTile(**layout_theme),
    # layout.TreeTab(
    #      font = "Ubuntu",
    #      fontsize = 10,
    #      sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
    #      section_fontsize = 10,
    #      border_width = 2,
    #      bg_color = "1c1f24",
    #      active_bg = "c678dd",
    #      active_fg = "000000",
    #      inactive_bg = "a9a1e1",
    #      inactive_fg = "1c1f24",
    #      padding_left = 0,
    #      padding_x = 0,
    #      padding_y = 5,
    #      section_top = 10,
    #      section_bottom = 20,
    #      level_shift = 8,
    #      vspace = 3,
    #      panel_width = 200
    #      ),
    layout.Floating(**layout_theme)
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=15,
    padding=0,
)
extension_defaults = widget_defaults.copy()

# screens = [
#     Screen(
#         top=bar.Bar(
#             [
#                 widget.GroupBox(
#                     active=gruvbox['fg9'],
#                     inactive=gruvbox['dark-gray'],
#                     highlight_method='line',
#                     block_highlight_text_color=gruvbox['dark-red'],
#                     borderwidth=0,
#                     highlight_color=gruvbox['tbg'],
#                     # background=gruvbox['fg1'],
#                     fontsize = 15,
#                     # margin_y = 1,
#                     # margin_x = 1,
#                     # padding_y = 0,
#                     # padding_x = 7,                    
#                 ),
#                 widget.Spacer(),
#                 widget.CurrentLayout(
#                             # background=gruvbox['fg0'],
#                             foreground=gruvbox['fg9'],
#                             fontsize = 15,
#                             ),
#                 widget.WindowCount(
#                             text_format='缾 {num}',
#                             # background=gruvbox['bg0'],
#                             foreground=gruvbox['fg9'],
#                             fontsize = 15,
#                             # show_zero=True,
#                             ),
#                 widget.Spacer(),
            
#                 # widget.CurrentLayout(),
#                 # widget.Prompt(),
#                 # widget.WindowName(),
#                 # widget.Mpris2(
#                 #     display_metadata=['xesam:title'],
#                 # ),
#                 widget.Chord(
#                     chords_colors={
#                         "launch": ("#ff0000", "#ffffff"),
#                     },
#                     name_transform=lambda name: name.upper(),
#                 ),
#                 # widget.Notify(),
#                 widget.Net(
#                     format = '{down} {up}',
#                     # background=gruvbox['fg1'],
#                     # foreground=gruvbox['dark-blue']
#                 ),
                
#                 widget.Clock(
#                     # background=gruvbox['fg0'],
#                     foreground=gruvbox['dark-magenta'],
#                     format=' %a, %b %d - %H:%M'
#                 ),
#                 # widget.QuickExit(),
#                 # widget.Volume(
#                 #     foreground = gruvbox['red'],
#                 #     # background = gruvbox['fg1'],
#                 #     fmt = ' {}',
#                 #     mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn("pavucontrol")}
#                 # ),
#                 widget.Systray(
#                     # background=gruvbox['fg0'],
#                     icon_size = 20,
#                 ),
#             ],
#                background=gruvbox['fg0'], size=26, margin=[0, 0, 0, 0],            
#         ),
#     ),
# ]

screens = [
    Screen(top=mera_bar1)
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
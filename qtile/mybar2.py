from libqtile import qtile
from libqtile import widget
from libqtile.bar import Bar
from colors import gruvbox
from unicodes import right_arrow, left_arrow, left_half_circle, lower_left_triangle

mera_bar1 = Bar([
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['fg1'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30
                    ),
                    widget.GroupBox(
                            active=gruvbox['fg9'],
                            inactive=gruvbox['dark-gray'],
                            highlight_method='line',
                            block_highlight_text_color=gruvbox['dark-red'],
                            borderwidth=0,
                            highlight_color=gruvbox['tbg'],
                            background=gruvbox['fg1'],
                            fontsize = 15,
                            margin_y = 1,
                            margin_x = 1,
                            padding_y = 0,
                            padding_x = 3,
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg1'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg'],
                            padding = 0,
                            fontsize = 25
                    ),
                    
                    widget.Spacer(),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg'],
                            padding = 0,
                            fontsize = 25
                    ),                   

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.CurrentLayout(
                            background=gruvbox['fg0'],
                            foreground=gruvbox['fg9']
                    ),                    
                    widget.WindowCount(
                            text_format=' {num}',
                            background=gruvbox['fg0'],
                            foreground=gruvbox['fg9'],
                            show_zero=True,
                    ),
                    
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                        #     background = gruvbox['fg1'],
                            foreground = gruvbox['fg'],
                            padding = 0,
                            fontsize = 25
                    ),

                    widget.Spacer(),
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                        #     background = gruvbox['fg1'],
                            foreground = gruvbox['fg'],
                            padding = 0,
                            fontsize = 25
                    ),
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg1'],
                            padding = 0,
                            fontsize = 30
                    ),
                    widget.Net(
                            format = ' {down} ↓↑{up}',
                            background=gruvbox['fg1'],
                            foreground=gruvbox['dark-blue']
                    ), 
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['fg1'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30
                    ),                                              
                    widget.Clock(
                            background=gruvbox['fg0'],
                            foreground=gruvbox['dark-magenta'],
                            format=' %a,%b%d-%H:%M'
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['fg0'],
                            foreground = gruvbox['fg1'],
                            padding = 0,
                            fontsize = 30
                    ),                                    
                    widget.Volume(
                            foreground = gruvbox['red'],
                            background = gruvbox['fg1'],
                            fmt = ' {}',
                            mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn("pavucontrol")}
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['fg1'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30
                    ),                    
                    widget.Systray(
                            background=gruvbox['fg0'],
                            foreground = gruvbox['fg0'],
                            icon_size = 22,
                    )
                                       
            ],
               background=gruvbox['bg'], size=26, margin=[0, 0, 0, 0],
        )

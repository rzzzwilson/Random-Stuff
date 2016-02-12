#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import rumps


Version = '0.2'

Debug = True

# check battery period
TimerPeriod = 5

# charge/discharge arrows
UpArrow = u'\u21E7'
DownArrow = u'\u21E9'

#Battery = u'\u1F50B'
#Battery = unichr(0x1F50B)
#Battery = u"\U0x1F50B"
#Battery = '🔋'
Battery = 'Battery'

# threshold voltage
MinimumVoltage = 10500

# threshold percentage
MinimumPercent = 25

# threshold charge remaining
MinimumCharge = 1200

# True if we have warned before
HaveWarned = False
WarnCount = 1

# warning voice
Voice = 'Zarvox'


class PowerApp(rumps.App):

    def __init__(self):
        super(PowerApp, self).__init__(Battery)
        self.menu = ['About']

    @rumps.clicked('About')
    def prefs(self, _):
        rumps.alert(title='Battery %s' % Version,
                    message='Battery is a system tray application that monitors the battery state.',
                    ok='OK')

    @rumps.timer(TimerPeriod)
    def repeating_function(self, sender):
        """Periodically check battery state."""

        global HaveWarned, WarnCount

        # get battery percent charge
        cmd = 'pmset -g batt | grep "InternalBattery" | awk \'{ print $2 }\' | sed "s/\;//"'
        percent = os.popen(cmd).read().strip()
        percent = int(percent[:-1])      # strip trailing '%', convert to int

        # get battery voltage
        cmd = 'system_profiler SPPowerDataType | grep "Voltage" | awk \'{print $3}\''
        voltage = int(os.popen(cmd).read().strip())

        # get 'charging' state
        cmd = 'pmset -g batt | grep "Now drawing from" | grep "AC Power"'
#        cmd = 'system_profiler SPPowerDataType | grep "Charging: Yes"'
        charging = (len(os.popen(cmd).read().strip()) > 0)

        # get remaining power left
        cmd = 'system_profiler SPPowerDataType | grep "Charge Remaining" | awk \'{print $4}\''
        charge = int(os.popen(cmd).read().strip())

        # update the tray title
        title = '%s %d%%%s' % (Battery, percent, UpArrow if charging else DownArrow)
        self.title = title

        if charging:
            HaveWarned = False
            WarnCount = 1

        print('voltage=%d, charge=%d, percent=%d%%, charging=%s, HaveWarned=%s, WarnCount=%d'
              % (voltage, charge, percent, str(charging), str(HaveWarned), WarnCount))

        # if empty, alert
        if (voltage < MinimumVoltage
                or percent < MinimumPercent
                or charge < MinimumCharge):
            # maybe warn
            #if not charging and not HaveWarned:
            if not charging:
                HaveWarned = True
                WarnCount -= 1
                if WarnCount == 0:
                    os.system('say -v "%s" "battery"&' % Voice)
                    WarnCount = 4
                extra = []
                if voltage < MinimumVoltage:
                    extra.append('voltage %d < %d' % (voltage, MinimumVoltage))
                if percent < MinimumPercent:
                    extra.append('percent %d < %d' % (percent, MinimumPercent))
                if charge < MinimumCharge:
                    extra.append('charge %d < %d' % (charge, MinimumCharge))
                extra = ', '.join(extra)
                msg = 'The battery is empty, please plug in.'
                if Debug:
                    rumps.notification('Battery %s' % Version, msg, '\n'+extra)
                else:
                    rumps.notification('Battery %s' % Version, msg, ' ')
#                rumps.alert(title='Battery %s' % Version, message=msg, ok='OK')
#                os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

if __name__ == '__main__':
    PowerApp().run()

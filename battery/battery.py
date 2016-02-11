#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import rumps


Version = '0.1'
TimerPeriod = 30
LastChargeState = None

#MinimumVoltage = 10500
MinimumVoltage = 12000


class PowerApp(rumps.App):

    def __init__(self):
        super(PowerApp, self).__init__('Battery')
        self.menu = ['About']

    @rumps.clicked('About')
    def prefs(self, _):
        rumps.alert(title='Power %s' % Version,
                    message="Power is a system tray appliction that monitors the battery state.",
                    ok='OK')

    @rumps.timer(TimerPeriod)
    def repeating_function(self, sender):
        """Periodically check battery state."""

        # get battery percent charge
        cmd = 'pmset -g batt | grep "InternalBattery" | awk \'{ print $2 }\' | sed "s/\;//"'
        percent = os.popen(cmd).read().strip()
        self.title = 'Battery %s' % percent

        # get battery voltage
        cmd = 'system_profiler SPPowerDataType | grep "Voltage" | awk \'{print $3}\''
        voltage = int(os.popen(cmd).read().strip())

        # get 'charging' state
        cmd = 'system_profiler SPPowerDataType | grep "Charging: Yes"'
        charging = (len(os.popen(cmd).read().strip()) > 0)

        # get 'charging' state
        cmd = 'system_profiler SPPowerDataType | grep "Charge Remaining" | awk \'{print $4}\''
        remaining = int(os.popen(cmd).read().strip())

        print('voltage=%d, remaining=%d, charging=%s' % (voltage, remaining, str(charging)))

        # if empty, alert
        if voltage <= MinimumVoltage and not charging:
            rumps.alert(title='Power %s' % Version,
                        message="The battery is empty, please plug in.",
                        ok='OK')


if __name__ == '__main__':
    PowerApp().run()

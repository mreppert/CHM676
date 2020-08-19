from IPython.display import display_markdown
from datetime import date
import datetime

class schedule:
    def __init__(self, meetdays, start_date):
        self.events = []
        self.start_date = date.fromisoformat(start_date)
        self.last_date = self.start_date + datetime.timedelta(-1)
        self.holidays = []
        daycodes = 'MTWUFAS'
        self.weekdays = []
        for d in meetdays:
            found_code = False
            for n in range(0, len(daycodes)):
                if daycodes[n]==d:
                    self.weekdays.append(n)
                    found_code = True
            if found_code==False:
                print('Warning: Could not match string \"' + d + '\" to a weekday code')

    def next_free_date(self):
        foundDate = False
        for delta in range(1, 365):
            dt1 = self.last_date + datetime.timedelta(delta)
            
            # First check if class usually meets on this day
            isMeetDay = False
            for m in self.weekdays:
                if dt1.weekday()==m:
                    isMeetDay = True
            
            # If so, check if it's a holiday
            if isMeetDay:
                isHoliday = False
                for hol in self.holidays:
                    # If it is a holiday, add holiday to the list of events
                    if hol[0]==dt1:
                        isHoliday = True
                        holitem = content('holiday', hol[1])
                        holitem.date = hol[0]
                        self.events.append(holitem)
            
            # If it is a valid class day, break out of the loop
            if isMeetDay and (not isHoliday):
                foundDate = True
                break
        if foundDate:
            return dt1
        else:
            return -1
    
    def add_holiday(self, datestring, htitle):
        self.holidays.append([date.fromisoformat(datestring), htitle])
        # If we've already scheduled events LATER than the new holiday
        # we need to re-schedule:
        if self.last_date >= date.fromisoformat(datestring):
            old_event_list = self.events
            self.events = []
            self.last_date = self.start_date + datetime.timedelta(-1)
            for item in old_event_list:
                if item.cformat != 'holiday':
                    self.add_content(item)
                
    def add_content(self, item):
        dt = self.next_free_date()
        item.date = dt
        self.events.append(item)
        self.last_date = item.date
                
    def print_events(self):
        week = 0
        module = 0
        lastday = 8
        mdtext = ''
        for item in self.events:
            if item.isnew:
                module += 1
                mdtext += "\r"
                mdtext += '## Module ' + str(module) + " \r"
            if item.date.weekday() < lastday:
                week += 1
                mdtext += '#### Week ' + str(week) + "\r"
            lastday = item.date.weekday()
            datetext = " * " + item.date.strftime("%b %-d") + ": "
            
            
            if item.cformat=='holiday':
                titletext = '<span style="color:blue">' + item.title + '</span>'
            elif item.cformat=='lecture':
                titletext = item.title
            else:
                titletext = item.title
                
            if len(item.link)>0:
                titletext = '[' + titletext + '](' + item.link + ')'
                
                
            mdtext += datetext + titletext + " \r\r"
        display_markdown(mdtext, raw=True)
        
class content:
    def __init__(self, cformat, title, newtopic=False, link=''):
        self.cformat = cformat
        self.title = title
        self.link = link
        self.date = -1
        self.isnew = newtopic


def build_schedule_f2020(srcdir):
    schd = schedule('MWF', '2020-08-24')

    schd.add_holiday('2020-11-25', 'Thanksgiving')
    schd.add_holiday('2020-11-26', 'Thanksgiving')
    schd.add_holiday('2020-11-27', 'Thanksgiving')

    schd.add_holiday('2020-12-07', 'Finals')
    schd.add_holiday('2020-12-08', 'Finals')
    schd.add_holiday('2020-12-09', 'Finals')
    schd.add_holiday('2020-12-10', 'Finals')
    schd.add_holiday('2020-12-11', 'Finals')
    schd.add_holiday('2020-12-12', 'Finals')

    schd.add_content(content('lecture', 'Python Crash Course: Introduction', link=srcdir+'programming/definitions.ipynb', newtopic=True))
    schd.add_content(content('lecture', 'Python Crash Course: Python Arrays', link=srcdir+'programming/arrays.ipynb'))
    schd.add_content(content('lecture', 'Python Crash Course: Molecular Dynamics', link=srcdir+'programming/md.ipynb'))

    schd.add_content(content('lecture', 'Maxwell\'s equations and the Lorentz Force Law'))
    schd.add_content(content('lecture', 'Electromagnetic Waves in Vacuum'))
    schd.add_content(content('lecture', 'Fourier Transforms'))

    schd.add_content(content('lecture', 'Energy Content in EM Waves'))
    schd.add_content(content('lecture', 'Microscopic Electrodynamics: The Wave Equation'))
    schd.add_content(content('lecture', 'MD in an Electric Field'))

    schd.add_content(content('lecture', 'Ensemble-Averaged Fields'))
    schd.add_content(content('lecture', 'Langevin Dynamics'))
    schd.add_content(content('lecture', 'Material Polarization'))

    schd.add_content(content('lecture', 'Review'))
    schd.add_content(content('lecture', 'Review'))
    schd.add_content(content('lecture', 'Exam'))

    schd.add_content(content('lecture', 'Response Theory', newtopic=True))
    schd.add_content(content('lecture', 'Linear Response: Absorption Spectroscopy'))
    schd.add_content(content('lecture', 'IR Absorption Spectroscopy'))

    schd.add_content(content('lecture', '$n$-Wave Mixing'))
    schd.add_content(content('lecture', 'Nonlinear Spectroscopy'))
    schd.add_content(content('lecture', 'Morse Oscillator'))

    schd.add_content(content('lecture', 'Homogeneous vs. Inhomogenous Broadening'))
    schd.add_content(content('lecture', 'Hole Burning Spectroscopy'))
    schd.add_content(content('lecture', 'Motional Narrowing'))

    schd.add_content(content('lecture', 'Pump-Probe Spectroscopy'))
    schd.add_content(content('lecture', '2D Spectroscopy'))
    schd.add_content(content('lecture', 'Morse Oscillator Nonlinear Spectroscopy'))

    schd.add_content(content('lecture', 'Review'))
    schd.add_content(content('lecture', 'Review'))
    schd.add_content(content('lecture', 'Exam'))

    schd.add_content(content('lecture', 'Intro to Quantum Mechanics', newtopic=True))
    schd.add_content(content('lecture', 'Quantum Statistical Dynamics'))
    schd.add_content(content('lecture', 'Matrix Computations'))

    schd.add_content(content('lecture', 'The Harmonic Oscillator'))
    schd.add_content(content('lecture', 'Molecular Excitons'))
    schd.add_content(content('lecture', 'Amide I Spectroscopy: Harmonic Excitons'))

    schd.add_content(content('lecture', 'Pure Dephasing Models'))
    schd.add_content(content('lecture', 'Dissipation: Redfield and Forster Regimes'))
    schd.add_content(content('lecture', 'Energy Transfer in Photosynthesis'))

    schd.add_content(content('lecture', 'Kubo Expansion I'))
    schd.add_content(content('lecture', 'Kubo Expansion II'))

    schd.add_content(content('lecture', 'Arrow-Ladder Diagrams'))
    schd.add_content(content('lecture', 'Diagrammatic 2D Spectroscopy'))

    schd.add_content(content('lecture', 'Freedom!'))
    return schd
"""
Adapted from: http://www.datadependence.com/2016/04/how-to-build-gui-in-python-3/
"""

try:
    import tkinter as tk #Python 3.x
    from tkinter import ttk as ttk
except ImportError:
    import Tkinter as tk # Python 2.x
    import ttk as ttk

import tkMessageBox
from kbapi import sru

def representsInt(s):
    # Source: http://stackoverflow.com/a/1267145
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
class carrierEntry(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
 
    def on_quit(self):
        # Exits program.
        quit()
 
    def submit(self):
        # Fetch entered values (strip any leading / tralue whitespace characters)
        
        catid = self.catid_entry.get().strip()
        volumeNo = self.volumeNo_entry.get().strip()
        noVolumes = self.noVolumes_entry.get().strip()
        carrierTypeCode = self.v.get()
        
        # Lookup carrierType for carrierTypeCode value
        for i in self.carrierTypes:
            if i[1] == carrierTypeCode:
                carrierType = i[0]
        
         # Lookup catalog identifier
        sruSearchString = '"PPN=' + str(catid) + '"'
        response = sru.search(sruSearchString,"GGC")
        noGGCRecords = response.sru.nr_of_records
        
        if representsInt(volumeNo) == False:
            msg = "Volume number must be integer value"
            tkMessageBox.showerror("Type mismatch", msg)
        elif representsInt(noVolumes) == False:
            msg = "Number of volumes must be integer value"
            tkMessageBox.showerror("Type mismatch", msg)
        elif int(volumeNo) < 1:
            msg = "Volume number must be greater than or equal to 1"
            tkMessageBox.showerror("Value error", msg)
        elif int(volumeNo) > int(noVolumes):
            msg = "Volume number cannot be larger than number of volumes"
            tkMessageBox.showerror("Value error", msg)
        elif noGGCRecords == 0:
            # No matching record found
            msg = ("Search for PPN=" + str(catid) + " returned " + \
                "no matching record in catalog!")
            tkMessageBox.showerror("PPN not found", msg)
        else:
            # Matching record found. Display title and ask for confirmation
            record = next(response.records)
            title = record.titles[0]
            msg = "Found title:\n\n'" + title + "'.\n\n Is this correct?"
            if tkMessageBox.askyesno("Confirm", msg):
                print(catid,volumeNo,noVolumes,carrierType)
                        
                # Reset entry fields
        
                self.catid_entry.delete(0, tk.END)
                self.volumeNo_entry.delete(0, tk.END)
                self.noVolumes_entry.delete(0, tk.END)
        
    def init_gui(self):
        # Build GUI
        self.root.title('iromlab')
        self.root.option_add('*tearOff', 'FALSE')
 
        self.grid(column=0, row=0, sticky='nsew')
 
        tk.Label(self, text='Enter carrier details').grid(column=0, row=0,
                columnspan=4)
       
        ttk.Separator(self, orient='horizontal').grid(column=0,
                row=1, columnspan=4, sticky='ew')
                
        # Catalog ID        
        tk.Label(self, text='PPN').grid(column=0, row=2,
                sticky='w')
        self.catid_entry = tk.Entry(self, width=12)
        self.catid_entry.grid(column=2, row = 2)

        # Volume number
        tk.Label(self, text='Volume number').grid(column=0, row=3,
                sticky='w')
        self.volumeNo_entry = tk.Entry(self, width=5)
        self.volumeNo_entry.grid(column=2, row=3)

        # Number of volumes
        tk.Label(self, text='Number of volumes').grid(column=0, row=4,
                sticky='w')
        self.noVolumes_entry = tk.Entry(self, width=5)
        self.noVolumes_entry.grid(column=2, row=4)
 
        # Carrier type (radio button select)
        self.v = tk.IntVar()
        self.v.set(1)
        
        tk.Label(self, text='Carrier type').grid(column=0, row=5,
                sticky='w', columnspan=4)
        
        # List with all possible carrier types + corresponding button codes
        self.carrierTypes = [
            ['cd-rom',1],
            ['cd-audio',2],
            ['dvd-rom',3],
            ['dvd-video',4]
        ]
        
        rowValue = 5
        
        for carrierType in self.carrierTypes:
            self.rb = tk.Radiobutton(self, text=carrierType[0], variable=self.v, value=carrierType[1]).grid(column=2, row=rowValue, 
            sticky='w')
            rowValue += 1
        
        self.submit_button = tk.Button(self, text='Submit',
                command=self.submit)
        self.submit_button.grid(column=0, row=11,  columnspan=3)
        
        self.submit_button = tk.Button(self, text='Quit',
                command=self.on_quit)
        self.submit_button.grid(column=2, row=11,  columnspan=3)
        
        """
        self.answer_frame = tk.LabelFrame(self, text='Answer',
                height=100)
        self.answer_frame.grid(column=0, row=12, columnspan=4, sticky='nesw')
 
        self.answer_label = tk.Label(self.answer_frame, text='')
        self.answer_label.grid(column=0, row=0)
        """
        
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
 
if __name__ == '__main__':
    root = tk.Tk()
    carrierEntry(root)
    root.mainloop()

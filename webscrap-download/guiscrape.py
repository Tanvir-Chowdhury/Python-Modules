from tkinter import *
from tkinter import filedialog, ttk, messagebox
import requests
from bs4 import BeautifulSoup
import base64
import json
import os

if __name__ == '__main__':
    _root = Tk()
    _root.title('Scrape app')
    _root.iconbitmap(r'D:\Python projects\Python-modules\Python-Modules\webscrap-download\Online_Scraper-512.png')
    
    _mainframe = ttk.Frame(_root, padding=(5, 5, 5, 5))
    _mainframe.grid(row = 0, column=0, sticky=(E, W, N, S))
    
    _url_frame = ttk.Labelframe(_mainframe, text = 'URL',padding=(5, 5, 5, 5))
    _url_frame.grid(row=0, column=0, sticky=(E, W))
    _url_frame.columnconfigure(0, weight=1)
    _url_frame.rowconfigure(0, weight=1)
    
    config = {}
    def fetch_url():
        url = _url.get()
        config['images'] =  []
        _images.set(())
        try: 
            page = requests.get(url)
        except Exception as e: 
            print(str(e))  
        else:  
            soup = BeautifulSoup(page.text, 'lxml')
            images = fetch_images(soup, url)
            if images:  
                _images.set(tuple(img['name'] for img in images))
                sb(f'images found : {len(images)}')
            else:  
                sb('No images found')
            config['images'] = images
    
    _url = StringVar()
    _url.set('Type your URL here...')
    _url_entry = ttk.Entry(_url_frame, width=40, textvariable=_url)
    _url_entry.grid(row=0, column=0, sticky=(E, W, N, S), padx=5)
    _fetch_btn = ttk.Button(_url_frame, text='Fetch info', command=fetch_url) 
    _fetch_btn.grid(row=0, column=1, sticky=W, padx=5)
    
    _image_frame = ttk.LabelFrame(_mainframe, text='Content', padding=(9, 0, 0, 0))
    _image_frame.grid(row=1, column=0, sticky='N, S, E,W')
    
    _images = StringVar()
    _img_listbox = Listbox(_image_frame, listvariable=_images, height=6, width=25)
    _img_listbox.grid(row=0, column=0, sticky=(E, W), pady = 5)
    _scrollbar = ttk.Scrollbar(_image_frame, orient=VERTICAL, command=_img_listbox.yview)
    _scrollbar.grid(row=0, column=1, sticky=(S, N), pady=6)
    _img_listbox.configure(yscrollcommand=_scrollbar.set)
    
    _radio_frame = ttk.Frame(_image_frame)
    _radio_frame.grid(row=0, column=2, sticky=(N, S, E, W))
    _choice_lbl = ttk.Label(_radio_frame, text="Choose how to save images :")
    _choice_lbl.grid(row=0, column=0, padx=5, pady=5)
    _save_method = StringVar()
    _save_method.set('img')
    _img_only_radio = ttk.Radiobutton(_radio_frame, text = 'As images', variable= _save_method, value='img')
    _img_only_radio.grid(row=1, column=0, padx=5, pady=2, sticky=W)
    _img_only_radio.configure(state='normal')
    _json_radio = ttk.Radiobutton(_radio_frame, text = 'As json', variable= _save_method, value='json')
    _json_radio.grid(row=2, column=0, padx=5, pady = 2,sticky=W)
    
    def save(): 
        if not config.get('images') :  
            _alert('no images to save')
            return
        if _save_method.get() == 'img':
            dirname = filedialog.askdirectory(mustexist=True)
            _save_images(dirname)
        else:  
            filename = filedialog.asksaveasfilename(initialfile = 'images.json', filetypes = ['JSON', '.json'])
            _save_json(filename)
    
    _scrape_btn = ttk.Button(_mainframe, text='Scrape!', command=save) 
    _scrape_btn.grid(row=2, column=0, sticky=E, pady=5)
    
    _status_frame = ttk.Frame(_root, relief='sunken', padding=(2, 2, 2, 2))
    _status_frame.grid(row=1, column=0, sticky=(E, W, S))
    _status_msg = StringVar()
    _status_msg.set('Type a URL to start scraping...')
    _status = ttk.Label(_status_frame, textvariable=_status_msg, anchor=W)
    _status.grid(row=0, column=0, sticky=(E, W))
    
    
    def fetch_images(soup, base_url): 
        images = []
        count = 0
        for img in soup.findAll('img'):
            src = img.get('src')
            img_url = f'{base_url}/{src}'
            name = 'photo' + str(count)
            images.append(dict(name=name, url=img_url))
            count += 1
        return images

    def _save_images(dirname):
        if dirname and config.get('images') :
            for img in config['images']:  
                img_data = requests.get(img['url']).content
                filename = os.path.join(dirname, img['name']+'.png')
                with open(filename, 'wb') as f:
                    f.write(img_data)
            _info('Done !')

    def _save_json(filename):  
        if filename and config.get('images'):  
            data = {}
            for img in config['images']:  
                img_data = requests.get(img['url'])
                bas64_image = base64.b64encode(img_data)
                str_image = bas64_image.decode('utf-8')
                data[img['name']] = str_image
                with open(filename, 'w') as ijson:  
                    ijson.write(json.dumps(data))
            _info('Done !')

    def sb(msg):  
        _status_msg.set(msg)

    def _alert(msg):
        messagebox.showerror(message=msg)

    def _info(msg):  
        messagebox.showinfo(message=msg)
        
    _root.mainloop()
import tkinter as tk

def main():
    width = 800
    height = 500

    root = tk.Tk()
    root.geometry(f'{width}x{height}')

    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    draw_night(canvas, 0,0,0)
    canvas.create_rectangle(400,0,799,499, fill='light sky blue')
    tree_center = scene_left + 200
    tree_top = scene_top + 300
    tree_height = 200
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    tree2_center= scene_left + 600
    tree2_top = scene_top + 300
    tree2_height = 200
    draw_pine_tree2(canvas,tree2_center,tree2_top,tree2_height)
    draw_sun(canvas, 600,100)
    draw_moon(canvas, 100,100)
    draw_cloud1(canvas, 450,200)
    draw_cloud2(canvas, 475,240)
    draw_cloud3(canvas,500,175)
    draw_cloud4(canvas, 25,250)
    draw_cloud5(canvas, 100,200)
    canvas.create_rectangle(0,480,799,499, fill="dark olive green")
    
def draw_pine_tree(canvas, peak_x, peak_y, height):
    
    trunk_width = height / 5
    trunk_height = height / 4
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    canvas.create_rectangle(trunk_left, skirt_bottom, trunk_right, trunk_bottom, outline="gray20", width=1, fill="tan3")
    canvas.create_polygon(peak_x, peak_y, skirt_right, skirt_bottom, skirt_left, skirt_bottom,outline="gray20", width=1, fill="dark green")


def draw_pine_tree2(canvas, peak_x, peak_y, height):
    
    trunk_width = height / 5
    trunk_height = height / 4
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    canvas.create_rectangle(trunk_left, skirt_bottom, trunk_right, trunk_bottom, outline="gray20", width=1, fill="tan3")
    canvas.create_polygon(peak_x, peak_y, skirt_right, skirt_bottom, skirt_left, skirt_bottom,outline="gray20", width=1, fill="dark green")

def draw_sun(canvas, sun_left, sun_top):
    sun_width = 100
    sun_height = 100
    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill='orange', width=False)

def draw_moon(canvas, moon_left, moon_top):
    moon_width = 100
    moon_height = 100
    moon_right = moon_left + moon_width
    moon_bottom = moon_top + moon_height
    canvas.create_oval(moon_left, moon_top, moon_right, moon_bottom, fill='AntiqueWhite1', width=False)

def draw_night(canvas, peak_x, peak_y, height):
    night_width = 400
    night_height = 500
    night_left = peak_x - night_width 
    night_right = peak_x + night_width
    night_bottom = peak_y + height
    
    canvas.create_rectangle(night_left, night_height, night_right, night_bottom, width=1, fill="blue2")

def draw_cloud1(canvas, cloud_left, cloud_top):
    cloud_width = 200
    cloud_height = 75
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height
    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill='white smoke', width=False)

def draw_cloud2(canvas, cloud_left, cloud_top):
    cloud_width = 50
    cloud_height = 50
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height
    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill='white smoke', width=False)

def draw_cloud3(canvas, cloud_left, cloud_top):
    cloud_width = 150
    cloud_height = 80
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height
    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill='white smoke', width=False)

def draw_cloud4(canvas, cloud_left, cloud_top):
    cloud_width = 200
    cloud_height = 90
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height
    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill='light slate grey', width=False)

def draw_cloud5(canvas, cloud_left, cloud_top):
    cloud_width = 150
    cloud_height = 80
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height
    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill='light slate grey', width=False)

main()
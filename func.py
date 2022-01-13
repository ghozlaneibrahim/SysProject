from exif import Image


class Location:
    longitude = 0
    latitude = 0


def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == 'S' or ref == 'W':
        decimal_degrees = -decimal_degrees
    return decimal_degrees


def image_coordinates(img_path):
    with open(img_path, 'rb') as src:
        img = Image(src)
        location = Location()
    if img.has_exif:
        try:
            img.gps_longitude
            location.latitude, location.longitude = [decimal_coords(img.gps_latitude,
                                                                    img.gps_latitude_ref),
                                                     decimal_coords(img.gps_longitude,
                                                                    img.gps_longitude_ref)]

            return location

        except AttributeError:

            return location
    else:

        return location

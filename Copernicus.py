#Descarga de datos del CDS

import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'format': 'netcdf',
        'product_type': 'monthly_averaged_reanalysis',
        'variable': 'skin_temperature',
        'year': [
            '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
            '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
            '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
            '2010', '2011', '2012', '2013', '2014', '2015',
         ],
        'month': [
            '12', '01', '02', '03',
        ],
        'time': '00:00',
    },
    'download.nc')
times = int(input('Nhập số giây: '))

hours = (times // 3600)
minutes = ((times % 3600) // 60)
seconds = ((times % 3600) % 60)

print('Times: {0}:{1}:{2}'.format(hours, minutes, seconds))
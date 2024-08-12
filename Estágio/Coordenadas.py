import folium

x = float(input("Digite a coordenada x: "))
y = float(input("Digite o coordenada y: "))
#Suas coordenadas -18.970522, -49.458981

m = folium.Map(location = [x, y], zoom_start = 15)

folium.Marker(location = [x,y]).add_to(m)

m.save('mapa.html')

print("coordenadas salvas em 'mapa.html'")
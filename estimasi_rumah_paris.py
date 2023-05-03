import pickle
import streamlit as st

model = pickle.load(open('estimasi_rumah_paris.sav', 'rb'))

st.title('_ESTIMASI HARGA RUMAH DI PARIS_')

##'cityCode, made, floors, squareMeters, basement, attic, garage, numPrevOwners, numberOfRooms, hasGuestRoom, hasYard, hasPool, isNewBuilt, hasStormProtector, hasStorageRoom, cityPartRange
cityCode = st.number_input('Kode POS')
made = st.number_input('Input Tahun Dibuat')
floors = st.number_input('Input Tingkat Rumah')
squareMeters = st.number_input('Input Ukuran Rumah (m2)')
basement = st.number_input('Input Luas Ruang Bawah Tanah')
attic = st.number_input('Input Luas Loteng')    
garage = st.number_input('Luas Garasi')
numPrevOwners = st.number_input('Input Jumlah Pemilik Sebelumnya')
numberOfRooms = st.number_input('Input Jumlah Kamar')
hasGuestRoom = st.number_input('Input Jumlah Kamar Tamu')
hasYard = st.number_input('Input Apakah Rumah Termasuk Halaman(Ya=1, Tidak=0)')
hasPool = st.number_input('Input Apakah Rumah Termasuk Kolam Renang(Ya=1, Tidak=0)')
isNewBuilt = st.number_input('Input Apakah Sudah Pernah Direnovasi(Ya=1, Tidak=0)')
hasStormProtector = st.number_input('Input Apakah Memiliki Pelindung Badai(Ya=1, Tidak=0)')
hasStorageRoom = st.number_input('Input Apakah Memiliki Gudang(Ya=1, Tidak=0)')
cityPartRange = st.number_input('Input Kisaran Nilai Murah Sampai Mahal(1-10)')

predict = ''

if st.button('Estimasikan Harga Rumah'):
    predict = model.predict(
        [[cityCode, made, floors, squareMeters, basement, attic, garage, numPrevOwners, numberOfRooms, hasGuestRoom, hasYard, hasPool, isNewBuilt, hasStormProtector, hasStorageRoom, cityPartRange]]
    )
    st.write ('Estimasi harga Rumah Di Paris dalam Euro : ', predict)
    st.write ('Estimasi harga Rumah Di Paris dalam Rupiah (IDR) :', predict*16245.61)
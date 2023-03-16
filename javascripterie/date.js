new Date()
// Thu Mar 16 2023 10:26:56 GMT+0100 (heure normale d’Europe centrale)
new Date(10)
// Thu Jan 01 1970 01:00:00 GMT+0100 (heure normale d’Europe centrale)
new Date(2022, 0 ,1)
// Sat Jan 01 2022 00:00:00 GMT+0100 (heure normale d’Europe centrale)
new Date(2022,0 ,32)

// Tue Feb 01 2022 00:00:00 GMT+0100 (heure normale d’Europe centrale)
new Date(2022,0,32).getTimezoneOffset

// getTimezoneOffset() { [native code] }

new Date().getUTCDate()
// 16

new Date().toISOString()
// '2023-03-16T09:30:28.534Z'

new Date().toUTCString()
// 'Thu, 16 Mar 2023 09:31:10 GMT'

new Date().toLocaleDateString()
'16/03/2023'

new Date().toLocaleDateString('fr-FR')
'16/03/2023'

new Date().toLocaleString('fr-FR')
'16/03/2023 10:32:16'

new Date().toLocaleTimeString()
'10:32:32'

new Date().toLocaleString(undefined, {dateStyle: 'medium', 'timeStyle': 'long'})
'16 mars 2023, 10:35:07 UTC+1'
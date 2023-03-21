new Date()
// Thu Mar 16 2023 10:26:56 GMT+0100 (heure normale d’Europe centrale)
new Date(10)
// Thu Jan 01 1970 01:00:00 GMT+0100 (heure normale d’Europe centrale)
new Date(2022, 0, 1)
// Sat Jan 01 2022 00:00:00 GMT+0100 (heure normale d’Europe centrale)
new Date(2022, 0, 32)

// Tue Feb 01 2022 00:00:00 GMT+0100 (heure normale d’Europe centrale)
new Date(2022, 0, 32).getTimezoneOffset

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

new Date().toLocaleString(undefined, { dateStyle: 'medium', 'timeStyle': 'long' })
'16 mars 2023, 10:35:07 UTC+1'







let originalArray = [
    {
        "id": "73mcSNpeiKuU76OF9ppDJrVfCuzkPzIfmPQqMbECP2e1NXnwBDPOXipJJDU",
        "date": "08/10/2023",
        "titre": "1th",

    },
    {
        "id": "y7y9NvWTd9ARQChw2JHill2V4h8suUq6mdVx4bT5OWoKtxsnXp3TTWzcc",
        "date": "01/01/2021",
        "titre": "2th",

    },
    {
        "id": "G8rLnfLM6x6qNNVTbJpc",
        "date": "08/03/2021",
        "titre": "3th",

    },
    {
        "id": "FG4gKxW3m2Q2OfhVTHlxulUbPHFaG7Vfh3KbwKXZNt1bHXl",
        "date": "10/03/2020",
        "titre": "4th",

    },
    {
        "id": "kev54bMtLcprtIifZR05VNx5BbxZlmpeuzkoIM84M878M8ARl3bXrs",
        "date": "05/05/2019",
        "titre": "5th",

    },
    {
        "id": "kev54bMtLcprtIifZR05VNx5BbxZlmpeuzkoIM84M878M8ARl3bXrs",
        "date": "05/01/2012",
        "titre": "6th",
    },
    {
        "id": "kev54bMtLcprtIifZR05VNx5BbxZlmpeuzkoIM84M878M8ARl3bXrs",
        "date": "05/07/2024",
        "titre": "7th",

    },
    {
        "id": "kev54bMtLcprtIifZR05VNx5BbxZlmpeuzkoIM84M878M8ARl3bXrs",
        "date": "25/05/2030",
        "titre": "8nth",

    }

]




let orderedArray = originalArray.map(obj => {
    let dateParts = obj.date.split('/');
    let newDate = new Date(`${dateParts[2]}-${dateParts[1]}-${dateParts[0]}`);
    return {
        ...obj,
        date: newDate.toLocaleDateString('fr-CA')
    };
});

orderedArray.sort((a, b) => new Date(b.date) - new Date(a.date));

let reformated = orderedArray.map(obj => {
    let dateParts = obj.date.split('/');
    let newDate = new Date(`${dateParts[2]}-${dateParts[1]}-${dateParts[0]}`);
    return {
        ...obj,
        date: newDate.toLocaleDateString('fr-FR')
    };
});


console.log(reformated)
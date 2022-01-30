let persons = [
    {id: 1, name: "Jan Kowalski"},
    {id: 2,name: "John Doe"},
    {id: 3,name: "Jarek Kaczka"}
];

let ages = [
    {person: 1, age: 18},
    {person: 2, age: 24},
    {person: 3, age: 666}
];

let locations = [
    {person: 1, country: "Poland"},
    {person: 3, country: "Poland"},
    {person: 2, country: "USA"}
];

function showArrays ()
{
    document.getElementById("persons").innerHTML = "<p>Persons:</p>" +
        JSON.stringify(persons, null, 2)
    document.getElementById("ages").innerHTML = "<p>Ages:</p>" +
        JSON.stringify(ages, null, 2)
    document.getElementById("locations").innerHTML = "<p>Locations:</p>" +
        JSON.stringify(locations, null, 2)
}

function calcAvg ()
{
    var counter = 0;
    var sum = 0;

    for (var age of ages)
    {
        for (var location of locations)
        {
            if (location['country'] == "Poland")
            {
                if (age['person'] == location['person'])
                {
                    counter += 1;
                    sum += age['age'];
                }
            }
        }
    }

    var avg = sum/counter;

    document.getElementById("avg").innerHTML = "<p>Average age for persons living in Poland:</p>" + avg;
}
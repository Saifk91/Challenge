iex> person = %{name: "Saif", pet: %{ type: %{ name: "cat", species: "persian", legs: 4}, name: "Lozy", age: 2}}
iex> get_in(person, [:pet, :type, :species])
"persian"
iex> person.pet.type.species
"persian"

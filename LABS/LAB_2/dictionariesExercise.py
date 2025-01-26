game = {
  "name": "Counter-Strike",
  "genre": "Shooter",
  "release_year": 2000
}
print(game.get("name"))

game = {
  "name": "Counter-Strike",
  "genre": "Shooter",
  "release_year": 2000
}
game["release_year"] = 2012

game = {
  "name": "Counter-Strike",
  "genre": "Shooter",
  "release_year": 2000
}
game["developer"] = "Valve"

game = {
  "name": "Counter-Strike",
  "genre": "Shooter",
  "release_year": 2000
}
game.pop("genre")

game = {
  "name": "Counter-Strike",
  "genre": "Shooter",
  "release_year": 2000
}
game.clear()

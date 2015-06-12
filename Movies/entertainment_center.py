import media
import fresh_tomatoes

shutterIsland = media.Movie("Toy Story",
						"A U.S Marshal investigates the disappearance of a murderess who escaped from a hospital for the criminally insane."
						,"http://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
						"https://www.youtube.com/watch?v=5iaYLCiq5RM")

dkr = media.Movie("The Dark Knight",
				"When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
				"http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
				"https://www.youtube.com/watch?v=EXeTwQWrcwY")

znmd = media.Movie("Zindagi Na Milegi Dobara",
					"Three friends decide to turn their fantasy vacation into reality after one of their number becomes engaged.",
					"http://upload.wikimedia.org/wikipedia/en/3/3d/Zindaginamilegidobara.jpg",
					"https://www.youtube.com/watch?v=61Vc46RbVOs")

inception = media.Movie("Inception",
						"A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
						"http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
						"https://www.youtube.com/watch?v=YoHD9XEInc0")

threeidiots = media.Movie("3 Idiots",
							"Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them \"idiots\".",
							"http://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
							"https://www.youtube.com/watch?v=K0eDlFX9GMc")
pkp = media.Movie("Pyaar Ka Punchnama",
					"After falling in love, three room-mates experience changes in their lives.",
					"http://upload.wikimedia.org/wikipedia/en/c/c4/Pyar_Ka_Punchnama.jpg",
					"https://www.youtube.com/watch?v=kBIrTv-59kw")


movies = [shutterIsland,dkr,znmd,inception,threeidiots,pkp]

fresh_tomatoes.open_movies_page(movies)
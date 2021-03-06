import fresh_tomatoes
import media


disaster_artist = media.Movie("Disaster Artist",
                              "Making of the film The Room",
                              "https://upload.wikimedia.org/wikipedia/en/c/c9/TheDisastorArtistTeaserPoster.jpg",
                              "https://www.youtube.com/watch?v=sPSJYXi7BWA")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come alive!",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

get_out = media.Movie("Get Out",
                     "A boyfriend visits his girlfriends parents house, and things take a dark turn.",
                     "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png",
                     "https://www.youtube.com/watch?v=DzfpyUB60YY")

red_sparrow = media.Movie("Red Sparrow",
                          "Russian spy exposing an American mole in Russia",
                          "https://upload.wikimedia.org/wikipedia/en/5/5a/Red_Sparrow.png",
                          "https://www.youtube.com/watch?v=PmUL6wMpMWw")

big_hero_6 = media.Movie("Big Hero 6",
                          "In San Fransokyo a boy and a robot make friends",
                          "https://vignette.wikia.nocookie.net/filmguide/images/b/bb/Big-hero-6-poster-baymax-hi-res.jpg/revision/latest?cb=20150222112242",
                          "https://www.youtube.com/watch?v=z3biFxZIJOQ"
                          )

black_panther = media.Movie("Black Panther",
                            "Son of the King of Wakanda returns home to claim the throne",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

moana = media.Movie("Moana",
                    "A girl, a chicken, and a demi god restore the island",
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")

shawshank = media.Movie("Shawshank Redemption",
                        "A curious escape from a prison, and Morgan Freeman's lovely voice",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

zootopia = media.Movie("Zootopia",
                       "A city of animals, a fox and bunny work together to solve a crime.",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

wonder_woman = media.Movie("Wonder Woman",
                           "Amazon warrior princess takes over World War II",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY&t=4s")

avengers_infinity_war = media.Movie("Avengers: Infinity War",
                                    "Avengers and the marvel gang face their greatest threat",
                                    "https://upload.wikimedia.org/wikipedia/en/9/90/Avengers_Infinity_War.jpg",
                                    "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

wreck_it_ralph = media.Movie("Wreck It Ralph",
                              "In video games, the bad guy gets his break",
                              "https://upload.wikimedia.org/wikipedia/en/1/15/Wreckitralphposter.jpeg",
                              "https://www.youtube.com/watch?v=87E6N7ToCxs")



movies = [disaster_artist, toy_story, get_out, red_sparrow, big_hero_6, black_panther, school_of_rock, moana, shawshank, zootopia, wonder_woman, avengers_infinity_war, wreck_it_ralph]
fresh_tomatoes.open_movies_page(movies)



                        


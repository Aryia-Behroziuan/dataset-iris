# iris
The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician, eugenicist, and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.[1] It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.[2] Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".[3] Fisher's paper was published in the journal, the Annals of Eugenics, creating controversy about the continued use of the Iris dataset for teaching statistical techniques today.  The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.
Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines.[5]

The use of this data set in cluster analysis however is not common, since the data set only contains two clusters with rather obvious separation. One of the clusters contains Iris setosa, while the other cluster contains both Iris virginica and Iris versicolor and is not separable without the species information Fisher used. This makes the data set a good example to explain the difference between supervised and unsupervised techniques in data mining: Fisher's linear discriminant model can only be obtained when the object species are known: class labels and clusters are not necessarily the same.[6]

Nevertheless, all three species of Iris are separable in the projection on the nonlinear and branching principal component.[7] The data set is approximated by the closest tree with some penalty for the excessive number of nodes, bending and stretching. Then the so-called "metro map" is constructed.[4] The data points are projected into the closest node. For each node the pie diagram of the projected points is prepared. The area of the pie is proportional to the number of the projected points. It is clear from the diagram (left) that the absolute majority of the samples of the different Iris species belong to the different nodes. Only a small fraction of Iris-virginica is mixed with Iris-versicolor (the mixed blue-green nodes in the diagram). Therefore, the three species of Iris (Iris setosa, Iris virginica and Iris versicolor) are separable by the unsupervising procedures of nonlinear principal component analysis. To discriminate them, it is sufficient just to select the corresponding nodes on the principal tree.
## Dataset iris
Data set

Iris setosa
The dataset contains a set of 150 records under five attributes - sepal length, sepal width, petal length, petal width and species.


Iris versicolor

Iris virginica

Spectramap biplot of Fisher's iris data set
Fisher's Iris data 
The iris data set is widely used as a beginner's dataset for machine learning purposes. The dataset is included in R (programming language) base and Python in the machine learning package Scikit-learn, so that users can access it without having to find a source for it.

R code illustrating usage
iris
class(iris)
### "data.frame"

iris3
class(iris3)
#"array"
Python code illustrating usage
from sklearn.datasets import load_iris

iris = load_iris()
iris
This code gives:

{'data': array([[5.1, 3.5, 1.4, 0.2],
                [4.9, 3. , 1.4, 0.2],
                [4.7, 3.2, 1.3, 0.2],
                [4.6, 3.1, 1.5, 0.2],
Several versions of the dataset have been published.[8]

See also
Classic data sets
References
 R. A. Fisher (1936). "The use of multiple measurements in taxonomic problems". Annals of Eugenics. 7 (2): 179–188. doi:10.1111/j.1469-1809.1936.tb02137.x. hdl:2440/15227.
 Edgar Anderson (1936). "The species problem in Iris". Annals of the Missouri Botanical Garden. 23 (3): 457–509. doi:10.2307/2394164. JSTOR 2394164.
 Edgar Anderson (1935). "The irises of the Gaspé Peninsula". Bulletin of the American Iris Society. 59: 2–5.
 A. N. Gorban, A. Zinovyev. Principal manifolds and graphs in practice: from molecular biology to dynamical systems, International Journal of Neural Systems, Vol. 20, No. 3 (2010) 219–232.
 "UCI Machine Learning Repository: Iris Data Set". archive.ics.uci.edu. Retrieved 2017-12-01.
 Ines Färber, Stephan Günnemann, Hans-Peter Kriegel, Peer Kröger, Emmanuel Müller, Erich Schubert, Thomas Seidl, Arthur Zimek (2010). "On Using Class-Labels in Evaluation of Clusterings" (PDF). In Xiaoli Z. Fern; Ian Davidson; Jennifer Dy (eds.). MultiClust: Discovering, Summarizing, and Using Multiple Clusterings. ACM SIGKDD.
 A.N. Gorban, N.R. Sumner, and A.Y. Zinovyev, Topological grammars for data approximation, Applied Mathematics Letters Volume 20, Issue 4 (2007), 382-386.
 Bezdek, J.C. and Keller, J.M. and Krishnapuram, R. and Kuncheva, L.I. and Pal, N.R. (1999). "Will the real iris data please stand up?". IEEE Transactions on Fuzzy Systems. 7 (3): 368–369. doi:10.1109/91.771092.
 ## Ronald Fisher
 Sir Ronald Aylmer Fisher FRS[4] (17 February 1890 – 29 July 1962) was a British statistician, geneticist, eugenicist, and professor.[5] For his work in statistics, he has been described as "a genius who almost single-handedly created the foundations for modern statistical science"[6] and "the single most important figure in 20th century statistics".[7] In genetics, his work used mathematics to combine Mendelian genetics and natural selection; this contributed to the revival of Darwinism in the early 20th-century revision of the theory of evolution known as the modern synthesis. For his contributions to biology, Fisher has been called "the greatest of Darwin’s successors".[8]

Fisher held strong views on race. Notably, he was a dissenting voice in the 1950 UNESCO statement The Race Question, insisting on racial differences.[9]:27

From 1919 onward, he worked at the Rothamsted Experimental Station for 14 years;[10] there, he analysed its immense data from crop experiments since the 1840s, and developed the analysis of variance (ANOVA). He established his reputation there in the following years as a biostatistician.

He is known as one of the three principal founders of population genetics. He outlined Fisher's principle, the Fisherian runaway and sexy son hypothesis theories of sexual selection. His contributions to statistics include promoting the method of maximum likelihood and deriving the properties of maximum likelihood estimators, fiducial inference, the derivation of various sampling distributions, founding principles of the design of experiments, and much more.


Contents
1	Early life and education
2	Career
2.1	Rothamsted Experimental Station, 1919–1933
2.2	University College London, 1933–39
2.3	University of Cambridge, 1940–1956
2.4	Adelaide, 1957–1962
3	Personal life and beliefs
4	Legacy
5	Recognition
6	Eugenics
7	Views on race
8	Bibliography
9	References
9.1	Citations
9.2	Sources
10	Further reading
11	External links
Early life and education

As a child

Inverforth House North End Way NW3, where Fisher lived from 1896 to 1904
Fisher was born in East Finchley in London, England, into a middle-class household; his father, George, was a successful partner in Robinson & Fisher, auctioneers and fine art dealers.[11] He was one of twins, with the other twin being still-born[12] and grew up the youngest, with three sisters and one brother.[13] From 1896 until 1904 they lived at Inverforth House in London, where English Heritage installed a blue plaque in 2002, before moving to Streatham.[14] His mother, Kate, died from acute peritonitis when he was 14, and his father lost his business 18 months later.[11]

Lifelong poor eyesight caused his rejection by the British Army for World War I,[15] but also developed his ability to visualize problems in geometrical terms, not in writing mathematical solutions, or proofs. He entered Harrow School age 14 and won the school's Neeld Medal in mathematics. In 1909, he won a scholarship to study Mathematics at Gonville and Caius College, Cambridge. In 1912, he gained a First in Mathematics.[16] In 1915 he published a paper The evolution of sexual preference[17] on sexual selection and mate choice.

Career
During 1913–1919, Fisher worked for six years as a statistician in the City of London and taught physics and maths at a sequence of public schools, at the Thames Nautical Training College, and at Bradfield College. There he settled with his new bride, Eileen Guinness, with whom he had two sons and six daughters.[18]

In 1918 he published "The Correlation Between Relatives on the Supposition of Mendelian Inheritance", in which he introduced the term variance and proposed its formal analysis.[19] He put forward a genetics conceptual model showing that continuous variation amongst phenotypic traits measured by biostatisticians could be produced by the combined action of many discrete genes and thus be the result of Mendelian inheritance. This was the first step towards establishing population genetics and quantitative genetics, which demonstrated that natural selection could change allele frequencies in a population, resulting in reconciling its discontinuous nature with gradual evolution.[20] Joan Box, Fisher's biographer and daughter says that Fisher had resolved this problem already in 1911.[21]

Rothamsted Experimental Station, 1919–1933
In 1919, he began working at the Rothamsted Experimental Station for 14 years,[10] where he analysed its immense data from crop experiments since the 1840s, and developed the analysis of variance (ANOVA). In 1919, he was offered a position at the Galton Laboratory in University College London led by Karl Pearson, but instead accepted a temporary job at Rothamsted in Harpenden to investigate the possibility of analysing the vast amount of crop data accumulated since 1842 from the "Classical Field Experiments". He analysed the data recorded over many years and in 1921, published Studies in Crop Variation, and his first application of the analysis of variance ANOVA.[22] In 1928, Joseph Oscar Irwin began a three-year stint at Rothamsted and became one of the first people to master Fisher's innovations. Between 1912 and 1922 Fisher recommended, analyzed (with heuristic proofs) and vastly popularized Maximum likelihood.[23]


On graduating from Cambridge University, 1912

The peacock tail in flight, the classic example of a Fisherian runaway

Rothamsted Research
Fisher's 1924 article On a distribution yielding the error functions of several well known statistics presented Pearson's chi-squared test and William Gosset's Student's t-distribution in the same framework as the Gaussian distribution and is where he developed Fisher's z-distribution, a new statistical method commonly used decades later as the F-distribution. He pioneered the principles of the design of experiments and the statistics of small samples and the analysis of real data.

In 1925 he published Statistical Methods for Research Workers, one of the 20th century's most influential books on statistical methods.[24] Fisher's method[25][26] is a technique for data fusion or "meta-analysis" (analysis of analyses). This book also popularized the p-value, and plays a central role in his approach. Fisher proposes the level p=0.05, or a 1 in 20 chance of being exceeded by chance, as a limit for statistical significance, and applies this to a normal distribution (as a two-tailed test), thus yielding the rule of two standard deviations (on a normal distribution) for statistical significance.[27] The 1.96, the approximate value of the 97.5 percentile point of the normal distribution used in probability and statistics, also originated in this book.

"The value for which P = 0.05, or 1 in 20, is 1.96 or nearly 2 ; it is convenient to take this point as a limit in judging whether a deviation is to be considered significant or not."[28]

In Table 1 of the work, he gave the more precise value 1.959964.[29]

In 1928, Fisher was the first to use diffusion equations to attempt to calculate the distribution of allele frequencies and the estimation of genetic linkage by maximum likelihood methods among populations.[30]

In 1930, The Genetical Theory of Natural Selection was first published by Clarendon Press and is dedicated to Leonard Darwin. A core work of the neo-Darwinian modern evolutionary synthesis,[31] it helped define population genetics, which Fisher founded alongside Sewall Wright and J. B. S. Haldane, and revived Darwin's neglected idea of sexual selection.[32]

One of Fisher's favourite aphorisms was "Natural selection is a mechanism for generating an exceedingly high degree of improbability."[33]

Fisher's fame grew and he began to travel and lecture widely. In 1931, he spent six weeks at the Statistical Laboratory at Iowa State College where he gave three lectures per week, and met many American statisticians, including George W. Snedecor. He returned there again in 1936.[citation needed]

University College London, 1933–39
In 1933, Fisher became the head of the Department of Eugenics at University College London.[34] In 1934, he become editor of the Annals of Eugenics (now called Annals of Human Genetics).

In 1935, he published The Design of Experiments, which was "also fundamental, [and promoted] statistical technique and application... The mathematical justification of the methods was not stressed and proofs were often barely sketched or omitted altogether .... [This] led H.B. Mann to fill the gaps with a rigorous mathematical treatment".[24][35] In this book Fisher also outlined the Lady tasting tea, now a famous design of a statistical randomized experiment which uses Fisher's exact test and is the original exposition of Fisher's notion of a null hypothesis.[36][37]

The same year he also published a paper on fiducial inference[38][39] and applied it to the Behrens–Fisher problem, the solution to which, proposed first by Walter Behrens and a few years later by Fisher, is the Behrens–Fisher distribution.

In 1936 he introduced the Iris flower data set as an example of discriminant analysis.[40]

In his 1937 paper The wave of advance of advantageous genes he proposed Fisher's equation in the context of population dynamics to describe the spatial spread of an advantageous allele and explored its travelling wave solutions.[41] Out of this also came the Fisher–Kolmogorov equation.[42] In 1937, he visited the Indian Statistical Institute in Calcutta, and its one part-time employee, P. C. Mahalanobis, often returning to encourage its development. He was the guest of honour at its 25th anniversary in 1957, when it had 2000 employees.[43]

In 1938, Fisher and Frank Yates described the Fisher–Yates shuffle in their book Statistical tables for biological, agricultural and medical research.[44] Their description of the algorithm used pencil and paper; a table of random numbers provided the randomness.

University of Cambridge, 1940–1956
In 1943, along with A.S. Corbet and C.B. Williams he published a paper on relative species abundance where he developed the logseries to fit two different abundance data sets[45] In the same year he took the Balfour Chair of Genetics where the Italian researcher Luigi Luca Cavalli-Sforza was recruited in 1948, establishing a one-man unit of bacterial genetics.

In 1936, Fisher used a Pearson's chi-squared test to analyze Mendel's data and concluded that Mendel's results with the predicted ratios were far too perfect, suggesting that adjustments (intentional or unconscious) had been made to the data to make the observations fit the hypothesis.[46] Later authors have claimed Fisher's analysis was flawed, proposing various statistical and botanical explanations for Mendel's numbers.[47][48] In 1947, Fisher cofounded the journal Heredity with Cyril Darlington and in 1949 he published The Theory of Inbreeding.

In 1950 he published "Gene Frequencies in a Cline Determined by Selection and Diffusion".[49] He developed computational algorithms for analyzing data from his balanced experimental designs,[50] with various editions and translations, becoming a standard reference work for scientists in many disciplines. In ecological genetics he and E. B. Ford showed how the force of natural selection was much stronger than had been assumed, with many ecogenetic situations (such as polymorphism) being maintained by the force of selection.

During this time he also worked on mouse chromosome mapping; breeding the mice in laboratories in his own house.[51]

Fisher publicly spoke out against the 1950 study showing that smoking tobacco causes lung cancer, arguing that correlation does not imply causation.[52][53][54][55][56][57] To quote his biographers Yates and Mather, "It has been suggested that the fact that Fisher was employed as consultant by the tobacco firms in this controversy casts doubt on the value of his arguments. This is to misjudge the man. He was not above accepting financial reward for his labours, but the reason for his interest was undoubtedly his dislike and mistrust of puritanical tendencies of all kinds; and perhaps also the personal solace he had always found in tobacco."[4]. Others, however, have suggested that his analysis was biased by professional conflicts and his own love of smoking[58].

He gave the 1953 Croonian lecture on population genetics.[59]

In the winter of 1954–1955 Fisher met Debabrata Basu, the Indian statistician who wrote in 1988, "With his reference set argument, Sir Ronald was trying to find a via media between the two poles of Statistics – Berkeley and Bayes.[60] My efforts to understand this Fisher compromise led me to the likelihood principle".[61]

Adelaide, 1957–1962

Memorial plaque over his remains, lectern-side aisle of St Peter's Cathedral, Adelaide
In 1957, a retired Fisher emigrated to Australia, where he spent time as a senior research fellow at the Australian Commonwealth Scientific and Industrial Research Organisation (CSIRO) in Adelaide. Following surgery for colon cancer, he died of post-operative complications in an Adelaide hospital in 1962.[62] His remains are interred in St Peter's Cathedral, Adelaide.[62]

Personal life and beliefs
He married Eileen Guinness, with whom he had two sons and six daughters.[18] His marriage disintegrated during World War II, and his older son George, an aviator, was killed in combat.[63] His daughter Joan, who wrote a biography of her father, married the statistician George E. P. Box.[64]


Stained glass window in the dining hall of Caius College, in Cambridge, commemorating Ronald Fisher and representing a Latin square, discussed by him in The Design of Experiments
According to Yates and Mather, "His large family, in particular, reared in conditions of great financial stringency, was a personal expression of his genetic and evolutionary convictions."[4] Fisher was noted for being loyal, and was seen as a patriot, a member of the Church of England, politically conservative, as well as a scientific rationalist. He developed a reputation for carelessness in his dress and was the archetype of the absent-minded professor. H. Allen Orr describes him in the Boston Review as a "deeply devout Anglican who, between founding modern statistics and population genetics, penned articles for church magazines".[65] In a 1955 broadcast on Science and Christianity,[4] he said:

The custom of making abstract dogmatic assertions is not, certainly, derived from the teaching of Jesus, but has been a widespread weakness among religious teachers in subsequent centuries. I do not think that the word for the Christian virtue of faith should be prostituted to mean the credulous acceptance of all such piously intended assertions. Much self-deception in the young believer is needed to convince himself that he knows that of which in reality he knows himself to be ignorant. That surely is hypocrisy, against which we have been most conspicuously warned.

Fisher was involved with the Society for Psychical Research.[66][67]

Legacy
Fisher's doctoral students included Walter Bodmer,[2] D. J. Finney,[2] Mary F. Lyon[3]and C. R. Rao[2] Although a prominent opponent of Bayesian statistics, Fisher was the first to use the term "Bayesian", in 1950.[68] The 1930 The Genetical Theory of Natural Selection is commonly cited in biology books, and outlines many important concepts, such as:

Parental investment, is any parental expenditure (time, energy etc.) that benefits one offspring at a cost to parents' ability to invest in other components of fitness,[69][70]
Fisherian runaway, explaining how the desire for a phenotypic trait in one sex combined with the trait in the other sex (for example a peacock's tail) creates a runaway evolutionary extremizing of the trait.
Fisher's principle, which explains why the sex ratio is mostly 1:1 in nature.
Reproductive value which implies that sexually reproductive value measures the contribution of an individual of a given age to the future growth of the population.[71][72]
Fisher's fundamental theorem of natural selection, which states that "the rate of increase in fitness of any organism at any time is equal to its genetic variance in fitness at that time."[73]
Fisher's geometric model, an evolutionary model of the effect sizes on fitness of spontaneous mutations proposed by Fisher to explain the distribution of effects of mutations that could contribute to adaptive evolution.[74]
Sexy son hypothesis, which hypothesizes that females may choose arbitrarily attractive male mates simply because they are attractive, thus increasing the attractiveness of their sons who attract more mates of their own. This is in contrast to theories of female mate choice based on the assumption that females choose attractive males because the attractive traits are markers of male viability.[75]
Mimicry, a similarity of one species to another that protects one or both
The evolution of dominance, a relationship between alleles of one gene, in which the effect on phenotype of one allele masks the contribution of a second allele at the same locus.[76]
Heterozygote advantage[77] which was later found to play a frequent role in genetic polymorphism.
Demonstrating that the probability of a mutation increasing the fitness of an organism decreases proportionately with the magnitude of the mutation and that larger populations carry more variation so that they have a greater chance of survival.
Fisher is also known for:

Linear discriminant analysis is a generalization of Fisher's linear discriminant[40][78]
Fisher information, see also scoring algorithm also known as Fisher's scoring, and Minimum Fisher information, a variational principle which, when applied with the proper constraints needed to reproduce empirically known expectation values, determines the best probability distribution that characterizes the system.[79]
F-distribution, arises frequently as the null distribution of a test statistic, most notably in the analysis of variance
Fisher–Tippett–Gnedenko theorem Fisher's contribution to this was made in 1927
Fisher–Tippett distribution
Von Mises–Fisher distribution[80]
Inverse probability, a term Fisher used in 1922, referring to "the fundamental paradox of inverse probability" as the source of the confusion between statistical terms which refer to the true value to be estimated, with the actual value arrived at by estimation, which is subject to error.[81]
Fisher's permutation test
Fisher's inequality[82]
Sufficient statistic, when a statistic is sufficient with respect to a statistical model and its associated unknown parameter if "no other statistic that can be calculated from the same sample provides any additional information as to the value of the parameter".[83]
Fisher's noncentral hypergeometric distribution, a generalization of the hypergeometric distribution, where sampling probabilities are modified by weight factors.
Student's t-distribution, widely used in statistics.[84][85]
The concept of an ancillary statistic and the notion (the ancillarity principle) that one should condition on ancillary statistics.
Recognition
Fisher was elected to the Royal Society in 1929. He was made a Knight Bachelor by Queen Elizabeth II in 1952 and awarded the Linnean Society of London Darwin–Wallace Medal in 1958.

He won the Copley Medal and the Royal Medal. He was an Invited Speaker of the ICM in 1924 in Toronto and in 1928 in Bologna.[86]

In 1950, Maurice Wilkes and David Wheeler used the Electronic Delay Storage Automatic Calculator to solve a differential equation relating to gene frequencies in a paper by Ronald Fisher.[87] This represents the first use of a computer for a problem in the field of biology. The Kent distribution (also known as the Fisher–Bingham distribution) was named after him and Christopher Bingham in 1982, while the Fisher kernel was named after Fisher in 1998.[88]

The R. A. Fisher Lectureship was a North American Committee of Presidents of Statistical Societies (COPSS) annual lecture prize, established in 1963, until the name was changed to COPSS Distinguished Achievement Award and Lectureship in 2020. On 28 April 1998 a minor planet, 21451 Fisher, was named after him.[89]

In 2010, the R.A. Fisher Chair in Statistical Genetics was established in University College London to recognise Fisher's extraordinary contributions to both statistics and genetics.

Anders Hald called Fisher "a genius who almost single-handedly created the foundations for modern statistical science",[6] while Richard Dawkins named him "the greatest biologist since Darwin":

Not only was he the most original and constructive of the architects of the neo-Darwinian synthesis, Fisher also was the father of modern statistics and experimental design. He therefore could be said to have provided researchers in biology and medicine with their most important research tools, as well as with the modern version of biology's central theorem.[90]

Geoffrey Miller said of him:

To biologists, he was an architect of the "modern synthesis" that used mathematical models to integrate Mendelian genetics with Darwin's selection theories. To psychologists, Fisher was the inventor of various statistical tests that are still supposed to be used whenever possible in psychology journals. To farmers, Fisher was the founder of experimental agricultural research, saving millions from starvation through rational crop breeding programs.[91]

Eugenics

As a steward at the First International Eugenics Conference, 1912
In 1911 Fisher became founding Chairman of the University of Cambridge Eugenics Society, whose other founding members included John Maynard Keynes, R. C. Punnett, and Horace Darwin. After members of the Cambridge Society – including Fisher – stewarded the First International Eugenics Congress in London in summer 1912, a link was forged with the Eugenics Society (UK).[92] He saw eugenics as addressing pressing social and scientific issues that encompassed and drove his interest in both genetics and statistics. During World War I Fisher started writing book reviews for The Eugenics Review and volunteered to undertake all such reviews for the journal, being hired for a part-time position.

The last third of The Genetical Theory of Natural Selection focused on eugenics, attributing the fall of civilizations to the fertility of their upper classes being diminished, and used British 1911 census data to show an inverse relationship between fertility and social class, partly due, he claimed, to the lower financial costs and hence increasing social status of families with fewer children. He proposed the abolition of extra allowances to large families, with the allowances proportional to the earnings of the father. [93][94][95] He served in several official committees to promote eugenics, including the Committee for Legalizing Eugenic Sterilization which drafted legislation aiming to limit the fertility of "feeble minded high-grade defectives ... comprising a tenth of the total population".[96][97]

In 1934, he resigned from the Eugenics Society over a dispute about increasing the power of scientists within the movement.[citation needed]

Fisher held a favourable view of eugenics even after World War II, when he wrote a testimony on behalf of the Nazi-associated eugenicist Otmar Freiherr von Verschuer, whose students had included Josef Mengele who conducted experiments at Auschwitz. Fisher wrote that he has no doubt that the Nazi party "sincerely wished to benefit the German racial stock, especially by the elimination of manifest defectives" and that he would give "his support to such a movement".[98]

In June 2020, Gonville and Caius College announced that a 1989 stained-glass window commemorating Fisher's work would be removed because of his connection with eugenics.[99]

Views on race
Further information: The Race Question
Between 1950 and 1951, Fisher, along with other leading geneticists and anthropologists of his time, was asked to comment on a statement that UNESCO was preparing on the "Nature of Race and Racial Differences". The statement, along with the comments and criticisms of a large number of scientists including Fisher, is published in "The Race Concept: Results of an Inquiry."[9]

Fisher was one of four scientists who opposed the statement. In his own words, Fisher's opposition is based on "one fundamental objection to the Statement," which "destroys the very spirit of the whole document." He believes that human groups differ profoundly "in their innate capacity for intellectual and emotional development" and concludes from this that the "practical international problem is that of learning to share the resources of this planet amicably with persons of materially different nature, and that this problem is being obscured by entirely well-intentioned efforts to minimize the real differences that exist."[100][101][102]

Fisher's opinions are clarified by his more detailed comments on Section 5 of the statement, which are concerned with psychological and mental differences between the races. Section 5 concludes as follows:

Scientifically, however, we realized that any common psychological attribute is more likely to be due to a common historical and social background, and that such attributes may obscure the fact that, within different populations consisting of many human types, one will find approximately the same range of temperament and intelligence.[9]:14

Of the entire statement, Section 5 recorded the most dissenting viewpoints. It was recorded that "Fisher's attitude … is the same as Muller's and Sturtevant's".[9]:56 Muller's criticism was recorded in more detail and was noted to "represent an important trend of ideas":

I quite agree with the chief intention of the article as a whole, which, I take it, is to bring out the relative unimportance of such genetic mental differences between races as may exist, in contrast to the importance of the mental differences (between individuals as well as between nations) caused by tradition, training and other aspects of the environment. However, in view of the admitted existence of some physically expressed hereditary differences of a conspicuous nature, between the averages or the medians of the races, it would be strange if there were not also some hereditary differences affecting the mental characteristics which develop in a given environment, between these averages or medians. At the same time, these mental differences might usually be unimportant in comparison with those between individuals of the same race…. To the great majority of geneticists it seems absurd to suppose that psychological characteristics are subject to entirely different laws of heredity or development than other biological characteristics. Even though the former characteristics are far more influenced than the latter by environment, in the form of past experiences, they must have a highly complex genetic basis.[9]:52

Fisher's own words were quoted as follows:

As you ask for remarks and suggestions, there is one that occurs to me, unfortunately of a somewhat fundamental nature, namely that the Statement as it stands appears to draw a distinction between the body and mind of men, which must, I think, prove untenable. It appears to me unmistakable that gene differences which influence the growth or physiological development of an organism will ordinarily pari passu influence the congenital inclinations and capacities of the mind. In fact, I should say that, to vary conclusion (2) on page 5, 'Available scientific knowledge provides a firm basis for believing that the groups of mankind differ in their innate capacity for intellectual and emotional development,' seeing that such groups do differ undoubtedly in a very large number of their genes.[9]:56

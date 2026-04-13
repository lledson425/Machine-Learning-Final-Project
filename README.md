# Machine-Learning-Final-Project
Group Members: Liam Edson

Abstract:
As we learn about next token prediction, I am very interested in seeing if I can build a model that can perform algebraic transformations and produce well formatted LaTeX code. I plan on building a synthetic training dataset that has valid algebraic equations as the input along with a valid next step in solving the equation as the target, and then tokenizing the data. Success will be measured by the model’s ability to produce sensible algebraic equations in LaTeX and to perform the next logical steps when solving unseen equations.

Motivation and Question:
The main motivating question is whether I can construct a model that can learn the rules of algebra and produce LaTeX. I am interested in this in large part because of the dataset that this will require. I think it will be an interesting challenge to write a script to create synthetic, formatted LaTeX. My previous research in machine learning has taken a similar form, investigating whether a model is able to learn the structure of data with externally imposed rules. I enjoy exploring this type of question, and I write a lot of algebra and LaTeX, so this project aligns well with my interests.
More specifically, for generating the data, my current plan is to use the SymPy package to generate the dataset. I want the dataset to look something like 3x + 5 = 11 ->, with the target sequence being 3x = 6. I will start with one variable linear equations to see if I can get that working, and then add complexity if needed.

Planned Deliverables:
My full success deliverables will include a Python script that can generate the synthetic LaTeX dataset to a desired level of complexity, a Python package that contains my model for next token prediction, and a Jupyter notebook that demonstrates the model’s capabilities. I am highly confident that even with partial success, I will be able to generate the equations and produce a model that outputs LaTeX, even if it is somewhat gibberish.

Resources Required:
Since I will be generating my own dataset, the only resource I may need is computational power. I currently have a Colab Pro subscription through the school and SSH access to more powerful computers if necessary, so I should not need additional resources.

What You Will Learn:
I am hoping to learn more about the SymPy package, as it seems like a powerful and interesting Python library. I also want to learn more about how to build next token prediction models that can perform specific tasks, especially given the recent prominence of these models.

Risk Statement:
One risk that could prevent me from completing this project fully is the possibility that I am unable to generate the dataset I want. Another potential risk is the uncertainty of the difficulty of this learning task. While the structure of this data is clear to a human, I am not sure how easily I will be able to train a model to produce non gibberish equations.

Ethics Statement:
We are already living in a world where the kinds of systems I plan to implement exist and are far more advanced than what I could hope to build. Highly advanced next token prediction models have already changed how work and productivity are approached. Fully functional algebraic solvers have also impacted educational practices, and this project would not be any different. This project does not directly engage with human centered decision making and instead relies on synthetic data. Even in an ideal scenario where I achieve all my goals, I believe the broader world would remain largely unchanged by this project.
Tentative Timeline:
Since we have not yet covered next token generation in class, I will wait two weeks before beginning work on the learning component of the project. In the meantime, I plan to make progress on building a script to generate the dataset.


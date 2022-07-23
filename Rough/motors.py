

# Step 4: Define a class for Steering Motor.
class SteeringMotor:
    """SteeringMotor(plus, minus, pot)

    A class to represent a Steering Motor.

    Attributes
    ----------
    plus : type = pyfirmata.pyfirmata.Pin
        The plus pin of the steering motor.
        This is a PWM output pin.
    minus : type = pyfirmata.pyfirmata.Pin
        The minus pin of the steering motor.
        This is a non-PWM output pin.
    pot : type = pyfirmata.pyfirmata.Pin
        The input pin which the potentiometer is connected to.
    name : str
        This is a string defining position of this steering motor.
        This variable will only help in debugging purpose.
        for example, for the front left steering motor:
            name = "Front Left"

    Methods
    -------
        # complete this
        get_position() :
            Returns current position of the steering motor in degrees.
        move(v,t=1) :
            Dynamically rotates the steering motor based on velocity and time.
        goto(position) :
            Rotates the motor to a specific angle at full speed.
    """

    def __init__(self, plus, minus, pot, name="Unknown"):
        """
        Construct all the necessary attributes of a Steering wheel.
        This function runs every time an instance of a steering motor is created.

        Parameters
        ----------
        plus : type = pyfirmata.pyfirmata.Pin
            The plus pin of the steering motor.
            This is a PWM output pin.
        minus : type = pyfirmata.pyfirmata.Pin
            The minus pin of the steering motor.
            This is a non-PWM output pin.
        pot : type = pyfirmata.pyfirmata.Pin
            The input pin the potentiometer is connected to.
        name : str
            This is a string defining position of this steering motor.
            for example, for the front left steering motor:
                name = "Front Left"
        """
        self.plus = plus
        self.minus = minus
        self.pot = pot
        self.name = name
        self.current_position = self.get_position()

    def get_position(self):
        """
        Reads the potentiometer value and Returns the current position of the
        steering motor in degrees. Its value is between 0 and 360 degrees.

        Parameters
        ----------
        None

        Variables
        ---------
        ll :

        ul :

        Returns
        -------
        The angle (float) of the steering motor
        """
        # some code will be here which will do the job, but you don't need to
        # do this right now! It will be done once the Rover is up and running.
        # for now, we are just going to return a linear function.
        #
        ll = 0.1  # lower limit of x (>=0)
        ul = 0.9  # upper limit of x (<=1)
        # x = self.pot.read()  # x ∈ [ll, ul] (closed interval)
        x = 0.69
        return 360 * (x - ll) / (ul - ll)

    def move(self, v, t=1):  # t in seconds
        """
        Moves the motors base on given speed for a certain time.
        We have assumed that positive velocity is counterclockwise and
        negative velocity is clockwise

        Parameters
        ----------
        v : type float
            Velocity of motor from speed 100 counterclockwise to 100 clockwise
            Ranges from 100 to -100
        t : type float
            Duration (in seconds) for which the the motor rotates

        Variables
        ---------
        pd : type float
            Potential that has to be be given to the plus(pwm pin). Calculates as-
                    pd = v/100.0      to implement positive/counterclockwise velocity
                    pd = 1+v/100.0    to implement negative/clockwise velocity (here, v is itself negative)
            Note: PWM output in pyfirmata takes values from 0 to 1
                  This translates to 0V to 5V in Arduino

        Returns
        -------
        Nothing

        """
        # write the appropriate docstrings here
        # write code for moving the motor clockwise for t seconds at speed v (v ∈ [-100, 100]).
        # Meaning of "Speed":
        #       The potenial difference between self.plus and self.minus = 5v/100 = pd (say)
        # If v is positive, the motor will move counterclockwise and self.minus will be at 0V and
        # self.plus will be at pd. Similarly if v is negative, the motor will move clockwise
        # and self.minus will be at 5V and self.plus will be at (5-pd)V. (don't forget self.minus can
        # only have binary values, 0V  and 5V and self.plus can only have values between 0V and 5V)
        #
        if v >= 0:              # positve velocity -> counterclockwise
            pd = v / 100.0        # higher potential for PWM(plus) pin
            self.plus.write(pd)
            self.minus.write(0)
        else:                   # negative velocity -> clockwise
            pd = 1 + v / 100.0      # lower potential for PWM(plus) pin (*v is itself negative)
            self.plus.write(pd)
            self.minus.write(1)
        time.sleep(t)           # moves till this time ends
        self.plus.write(0)      # the values are reinitialized to 0
        self.minus.write(0)

    def goto(self, position):
        """
        Rotates the motor to a certain angular position

        Parameters
        ----------
        position : type float
            The angular position to direct at

        Variables
        ---------
        difference : type float
            The required angle to rotate.
            If difference > 0
                then move counter-clockwise by difference (in degrees)
            If difference < 0
                then move clockwise by diffrence (in degrees)

        Returns
        -------
        Nothing

        """
        started_from = self.get_position()
        error=0 #need to be updated
        # write the appropriate docstrings here
        # position is a float/integer between 0 and 360 degrees
        # objective of this function is to move the steering motor to the required position
        #
        # Process: Start by calculating the difference between the current position and the
        # required position (say θ degrees). Call the move() function in full speed
        # (v = 100 if θ > 0 and v = -100 if θ < 0) for t = 1s. Then proportionally decrease the speed
        # of the motor with respect to the new distance (θnew) and call move(). Continue until the
        # [required position ± ERROR (defined at the beginning)] is reached.
        #
        v = 100   # initializing to full speed
        while(True):    #move() is called atleast once
            self.move(v)
            difference = position - self.get_position()
            #incomplete
            if abs(difference) <= error:
                break
        print(f"The {self.name} steering motor moved to {round(position, 2)}° from {round(started_from, 2)}°")  # comment this line on completion


# =========-=========-=========-=========-=========-=========-=========-
# Step 5: similarly write a class for the Driving Motors
class DrivingMotor:
    # write the docstrings here
    """DrivingMotor(plus, minus, pot)

    A class to represent a Driving Motor.

    Attributes
    ----------
    plus : type = pyfirmata.pyfirmata.Pin
        The plus pin of the driving motor.
        This is a PWM output pin.
    minus : type = pyfirmata.pyfirmata.Pin
        The minus pin of the driving motor.
        This is a non-PWM output pin.
    steering : type = class '__main__.SteeringMotor'
        The steering motor instance corresponding to the driving motor.


    Methods
    -------
        # complete this
        forward(speed) :
            Rotates the motor with given speed to move forward.
        backward(speed) :
            Rotates the motor with given speed to move backward.
        stop() :
            Stops any movement in the motor.
    """

    def __init__(self, plus, minus, steering):
        """
        Construct all the necessary attributes of a driving wheel.
        This function runs every time an instance of a driving motor is created.

        Parameters
        ----------
        plus : type = pyfirmata.pyfirmata.Pin
            The plus pin of the steering motor.
            This is a PWM output pin.
        minus : type = pyfirmata.pyfirmata.Pin
            The minus pin of the steering motor.
            This is a non-PWM output pin.
        steering : type = class '__main__.SteeringMotor'
            The steering motor instance corresponding to the driving motor.

        """
        # Docstring
        self.plus = plus
        self.minus = minus
        self.steering = steering  # the instance of the SteeringMotor() corresponding to this motor will be passed
        self.name = steering.name

    def forward(self, speed):
        """
        Rotates the driving motor to move wheel forward

        Parameters
        ----------
        speed : type float
            The speed at which the motor rotates.
                Ranges form 0 to 100.

        Variables
        ---------
        pd : type float
        Potential that has to be be given to the plus(pwm pin). Calculates as-
                    pd = speed/100.0      to implement positive/counterclockwise/forward velocity
            Note: PWM output in pyfirmata takes values from 0 to 1
                  This translates to 0V to 5V in Arduino

        Returns
        -------
        Nothing

        """
        # complete and add docstring
        # starts this driving motor in forward direction in speed = speed
        # Note: let p = steering.get_position(). if p>180, forward will be equal to p<180 backward.
        #
        pd = speed / 100.0
        self.plus.write(pd)     # higer potential for PWM(plus) pin
        self.minus.write(0)

    def backward(self, speed):
        """
        Rotates the driving motor to move wheel backward

        Parameters
        ----------
        speed : type float
            The speed at which the motor rotates
                Ranges from 0 to 100 ???? or -100

        Variables
        ---------
        pd : type float
        Potential that has to be be given to the plus(pwm pin). Calculates as-
                    pd = 1-speed/100.0    to implement negative/cloclwise/backward velocity
            Note: PWM output in pyfirmata takes values from 0 to 1
                  This translates to 0V to 5V in Arduino

        Returns
        -------
        Nothing

        """
        # complete and add docstring
        # starts this driving motor in backward direction in speed = speed
        #
        pd = 1 - speed / 100.0
        self.plus.write(pd)     # higer potential for PWM(plus) pin
        self.minus.write(1)

    def stop(self):
        """
        Stops any movement in the driving motor

        Parameters
        ----------
        None

        Variables
        ---------
        None

        Returns
        -------
        Nothing

        """
        # complete and add docstring
        # stops the motor whichever direction it was moving in.
        self.plus.write(0)
        self.minus.write(0)


if __name__ == "__main__":
    from settings import *
    # fl = SteeringMotor(smflp, smflm, smflpot, "Front Left")  # initialising the front left steering motor

    # __FRONT MOTORS__
    # initialising the front left and front right steering motors
    SM_FL, SM_FR = SteeringMotor(sm_fl_p, sm_fl_n, pr_fl, "Front Left"), SteeringMotor(sm_fr_p, sm_fr_n, pr_fr, "Front Right")
    # initialising the front left and front right driving motors
    DM_FL, DM_FR = DrivingMotor(dm_fl_p, dm_fl_n, SM_FL), DrivingMotor(dm_fr_p, dm_fr_n, SM_FR)

    # __MIDDLE MOTORS__
    # initialising the middle left and middle right steering motors
    SM_ML, SM_MR = SteeringMotor(sm_ml_p, sm_ml_n, pr_ml, "Middle Left"), SteeringMotor(sm_mr_p, sm_mr_n, pr_mr, "Middle Right")
    # initialising the middle left and middle right driving motors
    SM_ML, SM_MR = DrivingMotor(dm_ml_p, dm_ml_n, SM_ML), DrivingMotor(dm_mr_p, dm_mr_n, SM_MR)

    # __BACK MOTORS__
    # initialising the back left and back right steering motors
    SM_BL, SM_BR = SteeringMotor(sm_bl_p, sm_bl_n, pr_bl, "Back Left"), SteeringMotor(sm_br_p, sm_br_n, pr_br, "Back Right")
    # initialising the back left and back right driving motors
    SM_BL, SM_BR = DrivingMotor(dm_bl_p, dm_bl_n, SM_BL), DrivingMotor(dm_br_p, dm_br_n, SM_BR)

    fl.goto(75.488)  # moving the front left steering motor to 75 degrees

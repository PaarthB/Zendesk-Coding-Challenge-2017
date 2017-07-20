# unit tests based on path, statement coverage and mocking

"""
description: Image processing functions
"""
import cv2


class ImageProcessorAdapter:
    """
    description: Adapter for any processing functions done on an image
    """

    def __init__(self):
        """
        description: initialises the ImageProcessorAdapter object.
        """

        # Converting to grayscale is needed because of a cv2 error.
        # supports only CV_8UC1 images when mode != CV_RETR_FLOODFILL
        # otherwise supports CV_32SC1 images only in function
        # cvStartFindContours.

        pass

    def deskew(self, image):

        # convert the image to grayscale and flip the foreground
        # and background to ensure foreground is now "white" and
        # the background is "black"
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.bitwise_not(gray)

        # threshold the image, setting all foreground pixels to
        # 255 and all background pixels to 0
        thresh = cv2.threshold(gray, 0, 255,
                               cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # grab the (x, y) coordinates of all pixel values that
        # are greater than zero, then use these coordinates to
        # compute a rotated bounding box that contains all
        # coordinates
        coords = np.column_stack(np.where(thresh > 0))
        angle = cv2.minAreaRect(coords)[-1]

        # the `cv2.minAreaRect` function returns values in the
        # range [-90, 0); as the rectangle rotates clockwise the
        # returned angle trends to 0 -- in this special case we
        # need to add 90 degrees to the angle
        if angle < -45:
            angle = -(90 + angle)

        # otherwise, just take the inverse of the angle to make
        # it positive
        else:
            angle = -angle

        # rotate the image to deskew it
        (height, width) = image.shape[:2]
        center = (width // 2, height // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (width, height),
                                 flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

        image = rotated
        # draw the correction angle on the image so we can validate it
        cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        return 0

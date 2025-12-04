def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    try:
      if int(zip_code) and len(zip_code) == 5:
            return True
    except (ValueError, TypeError):
            return False
print(is_valid_zip(1234))

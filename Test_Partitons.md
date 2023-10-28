
For identifying these test cases, we've sat down with the applications requirements specification and figured which values were valid or invalid. To design the test cases we have used the techniques learned from our classes, particularly Equivalence partitioning and Boundary Analysis. 
Equivalence partitioning might not be as clear as it could have been in this document, however we are using technique in the code base. 

#### First & Last name

**Valid partitions:**
1. **English**: Casper
12. **Danish**: Øjvind

**Invalid partitions**
1. **Casper1 (including a numeric value)**
2. **Ca#sper! (including special characters, not being an alphabetic difference )**
3. **"" (empty string)**
4. **" Casper" (starting with a space)**
5. **123512123 (only numeric values)**
6. 珀ØΚάσ (Mixing language characters. Here we used danish, chinese & greek)
8. **Hebrew (Modern)**: כספר
9. **Arabic**: كاسبر
10. **Russian**: Каспер
11. **Greek**: Κάσπερ
12. **Chinese**: 卡斯珀
13. **Japanese (Katakana)**: カスパー
14. **Korean (Hangul)**: 카스퍼
15. **Hindi (Transliteration)**: कैस्पर
16. **Persian (Farsi)**: کاسپر

#### Gender

**Valid partitions**
1. Male
2. Female
3. Other ??? (2023 life)


**Invalid partitions** 
1. " Male" 
2. "Male "
3. " Female"
4. "Female "
5. 34252
6. #!Male#!
7. /!Female"


#### CPR

**Valid partitons for a male**
1. 30.01.98 1111 (Date exists and last four indicates male)
2. 31.12.99 2323 (Last day of the decade)
3. 01.01.01 9923 (First day of the new decade)
4. 29.02.92 5799 (Leap year '92) 

**Invalid partitons for a male**
1. 32.01.20 1573 (Invalid day)
2. 01.13.20 3571 (Invalid month)
3. 29.02.93 5799 (29th Feb on a Non-leap year)
4. 31.12.01 0248 (Even final digit)
5. 30.06.X8 7391 (Non-numeric character)
6. 21.11.850 7135 (Extra digit)
7. 04.07.1 1359 (Missing digit)
8. 28.10.04 93A1 (Non-numeric character)
9. 12.31.04 9993 (Reversed format for date and month)

**Valid partitons for a female**
1. 30.01.98 1112 (Date exists and last four indicates male)
2. 31.12.99 2324 (Last day of the decade)
3. 01.01.01 9924 (First day of the new decade)
4. 29.02.92 5798 (Leap year '92) 

**Invalid partitons for a female**
1. 32.01.20 0246 (Invalid day)
2. 01.13.20 2468 (Invalid month)
3. 29.02.93 4682 (29th Feb on a Non-leap year)
4. 31.12.01 9157 (Odd final digit)
5. 30.06.9X 6248 (Non-numeric character)
6. 21.11.850 4860 (Extra digit)
7. 04.07.1 2684 (Missing digit)
8. 28.10.04 80B2 (Non-numeric character)
9. 12.31.04 0294 (Reversed format for date and month)

#### Date of birth - Based on CPR
 
 **Valid Partitions:**

1. **Exact Match**: The date of birth provided exactly matches the date extracted from the CPR.
    - Date of birth: 01/01/2020, CPR: **010120**20XXXX

**Invalid Partitions:**

1. **Mismatched Day**: The day part of the date doesn't match.
    - Date of birth: 02/01/2020, CPR: **010120**20XXXX
      
2. **Mismatched Month**: The month part of the date doesn't match.
    - Date of birth: 01/02/2020, CPR: **010120**20XXXX
      
3. **Mismatched Year**: The year part of the date doesn't match.
    - Date of birth: 01/01/2019, CPR: **010120**20XXXX
      
4. **Invalid Date Format**: The provided date of birth is in a different format.
    - Date of birth: 01-Jan-2020, CPR: **010120**20XXXX
    - Date of birth: January 1, 2020, CPR: **010120**20XXXX
    - Date of birth: 2020-01-01, CPR: **010120**20XXXX
    
1. **Leap Year Mismatch**: The CPR suggests a leap year date, but the provided date isn't a leap year, or vice versa.
    - Date of birth: 29/02/2019 (non-leap year), CPR: **290219**20XXXX 
      
6. **Invalid Day or Month Values**:
    - Date of birth: 32/01/2020 (Day value is invalid), CPR: **320120**20XXXX
    - Date of birth: 01/13/2020 (Month value is invalid), CPR: **011320**20XXXX
      
7. **Incomplete Date Information**:
    - Date of birth: 01/01/20 (year incomplete), CPR: **010120**20XXXX


#### Address

##### Street:

**Valid Partitions:**

1. A sequence of alphabetic characters also with language specific characters.
    - Example: "Elm"
    - Example: "Nørrebrograde"
    - Example: "王府井大街" (Wangfujing Street) Chinese
    - Example: "רחוב הכוכב" (HaKochav Street) Hebrew
    - More languages to add.....

**Invalid Partitions:**

1. Contains numeric digits or special characters.
    - Example: "Elm4", "Main$"
2. Empty or whitespace.
    - Example: "", " "

##### Number:

**Valid Partitions:**

1. A number between 1 and 999.
    - Example: "42"
    - Example: "1"
    - Example: "999"
1. A number between 1 and 999 followed by an uppercase letter.
    - Example: "42B"
    - Example: "1A"
    - Example: "999C"

**Invalid Partitions:**

1. Number below 1 or above 999.
    - Example: "0", "1000"
2. Followed by more than one letter or a lowercase letter.
    - Example: "42BB", "42b"
3. Contains special characters.
    - Example: "42#"

##### Floor:

**Valid Partitions:**

1. "st".
2. A number between 1 and 99.
    - Example: "12"
    - Example: "1"
    - Example: "99"

**Invalid Partitions:**

1. Number below 1 or above 99.
    - Example: "0", "100"
2. Contains letters other than "st".
    - Example: "1st", "sf", "2nd"

##### Door:

**Valid Partitions:**

1. "th", "mf", "tv".
2. A number between 1 and 50.
    - Example: "15"
    - Example: "1"
    - Example: "50"
1. A lowercase letter followed by a number between 1 and 999.
    - Example: "c3"
    -  Example: "1a"
    - Example: "50c"
1. A lowercase letter followed by a dash and a number between 1 and 999.
    - Example: "d-14"
    - Example "d-1"
    - Example: "d-999"

**Invalid Partitions:**

1. Uppercase letters or more than one letter.
    - Example: "C3", "cd3" **(??? How picky are we in terms of the specifications? Dosen't provide example of uppercase as valid)**
2. Number below 1 or above 50 (if it's only a number).
    - Example: "0", "51"
3. Number above 999 after a lowercase letter.
    - Example: "c1000"
4. Special characters (other than a single dash in the specified format).
    - Example: "c@3", "c3-5"


#### Postal Code

**Invalid partitons**
1. Special characters or letters.
	*  Example: 4000#, 40AB2
1. Lack of digits:
	*  Example: 302
2. Too many digits.
	* Example: 40001 

**Valid partitons**
1. Correct number of digits.
	* Example: 4000
	* Example: 0001
	* Example: 9999

#### Town

**Valid partitons:**
1. **English**: Sunville
2. **Hebrew (Modern)**: גבעת שמש (Giv'at Shemesh)
3. **Arabic**: وادي النور (Wadi Al-Noor)
4. **Russian**: Солнечный (Solnechny)
5. **Greek**: Ηλιόπολη (Iliópoli)
6. **Chinese (Transliteration)**: 阳光城 (Yángguāng Chéng)
7. **Japanese (Katakana)**: サンタウン (San Taun)
8. **Korean (Hangul)**: 해빛마을 (Hae-bit Maeul)
9. **Hindi (Transliteration)**: सूर्यनगर (Sūryanagar)
10. **Persian (Farsi)**: شهر آفتاب (Shahr-e Aftab)

**Invalid partitons:**
1. **Names with Numbers**:
    
    - For all languages, names that contain numbers would be invalid.
    - Examples:
        - English: Sunville1
        - Hebrew: גבעת1
        - Arabic: وادي1
        - ... and so on for the rest of the languages.
        - 
1. **Names with Special Characters not Belonging to the Language**:
    
    - Incorporating characters that are not part of the alphabet or standard script for each respective language.
    - Examples:
        - English: Sunville@ or Sunville- or Sunville!
        - Hebrew: גבעת@ or גבעת!
        - Arabic: وادي@ or وادي!
        - Russian: Солнечный@ or Солнечный!
        - ... and so on for the rest of the languages.
        - 
1. **Names with Characters from Another Language**:
    
    - Mixing characters from different languages.
    - Examples:
        - Using Latin characters in a Hebrew name: גבעתSun
        - Using Cyrillic characters in an Arabic name: واديСолн
        - ... and so on for the rest of the languages.
        - 
1. **Names with Only Spaces**:
    
    - Having a name that's purely whitespace or spaces.
    - Examples for all languages: " " (just spaces)
    
1. **Names with Leading or Trailing Spaces**:
    
    - This would be names that might look valid but have spaces at the beginning or end.
    - Examples:
        - English: " Sunville" or "Sunville "
        - Hebrew: " גבעת" or "גבעת "
        - ... and so on for the rest of the languages.
        
1. **Empty Names**:
    
    - No characters at all.


#### Phone number

**Valid Partitions:**

1. **Numbers Starting with Single Digits**:
    
    - Lower Boundary: 20000000
    - Upper Boundary: 29999999
2. **Numbers Starting with '30' or '31'**:
    
    - Lower Boundary: 30000000, 31000000
    - Upper Boundary: 30999999, 31999999
3. **Numbers Starting with '40' to '42'**:
    
    - Lower Boundary: 40000000
    - Upper Boundary: 42999999
    
    ... (Following similar patterns for the rest of the two-digit starting combinations...)
    
4. **Numbers Starting with '342'**:
    
    - Lower Boundary: 34200000
    - Upper Boundary: 34299999
5. **Numbers Starting with '344' to '349'**:
    
    - Lower Boundary: 34400000
    - Upper Boundary: 34999999
    
    ... (Following similar patterns for the rest of the three-digit starting combinations...)
    

**Invalid Partitions:**

1. **Numbers Less than 8 Digits**:
    
    - Example: 3000000
2. **Numbers More than 8 Digits**:
    
    - Example: 300000000
3. **Numbers not starting with specified combinations**:
    
    - Example (non-starters): 33000000, 34300000, 35000000, 54000000...
4. **Numbers with Characters other than Digits**:
    
    - Example: 3000A000
5. **Numbers with leading zeroes (assuming they are considered invalid due to less than 8 significant digits)**:
    
    - Example: 03000000

**Boundary Tests:**

1. **Lower Boundaries** for each valid partition. 
    
    - 20000000
    - 30000000
    - 31000000
    - 34200000
    - 34400000
    - ...
2. **Upper Boundaries** for each valid partition:
    
    - 29999999
    - 30999999
    - 31999999
    - 34299999
    - 34999999
    - ...
3. **Just Outside of Boundaries**: Test numbers just outside of valid ranges to ensure validation catches them.
    
    - 29999998, 30000001
    - 30999998, 31000001

import streamlit as st

st.title("Project")
st.write("## Data Description")
st.info("The source for this dataset is the **Sloan Digital Sky Survey (SDSS)**, one of the most comprehensive public sources of astronomical datasets available on the web today. SDSS has been one of the most successful surveys in astronomy history, having created highly detailed three-dimensional maps of the universe and curated spectroscopic and photometric information on over three million astronomical objects in the night sky. SDSS uses a dedicated 2.5 m wide-angle optical telescope which is located at the **Apache Point Observatory** in New Mexico, USA. ")

st.info("The survey was named after the Alfred P. Sloan Foundation (established by Alfred P. Sloan, ex-president of General Motors), a major donor to this initiative and among others, the MIT Sloan School of Management.")

st.info("The following dataset consists of 250,000 celestial object observations taken by SDSS. Each observation is described by 17 feature columns and 1 class column that identifies the real object to be one of **a star, a galaxy or a quasar.**")

columns = st.checkbox('Columns')

if columns:
    st.write("* **objid** = Object Identifier, the unique value that identifies the object in the image catalog used by the CAS")
    st.write("* **u** = Ultraviolet filter in the photometric system")
    st.write("* **ra** = Right Ascension angle (at J2000 epoch)")
    st.write("* **dec** = Declination angle (at J2000 epoch)")
    st.write("* **g** = Green filter in the photometric system")
    st.write("* **r** = Red filter in the photometric system")
    st.write("* **i** = Near-Infrared filter in the photometric system")
    st.write("* **z** = Infrared filter in the photometric system")
    st.write("* **run** = Run Number used to identify the specific scan")
    st.write("* **rerun** = Rerun Number to specify how the image was processed")
    st.write("* **camcol** = Camera column to identify the scanline within the run")
    st.write("* **field** = Field number to identify each field")
    st.write("* **specobjid** = Unique ID used for optical spectroscopic objects (this means that 2 different observations with the same spec_obj_ID must share the output class)")
    st.write("* **class** = object class (galaxy, star, or quasar object)")
    st.write("* **redshift** = redshift value based on the increase in wavelength")
    st.write("* **plate** = plate ID, identifies each plate in SDSS")
    st.write("* **mjd** = Modified Julian Date used to indicate when a given piece of SDSS data was taken")
    st.write("* **fiberid** = fiber ID that identifies the fiber that pointed the light at the focal plane in each observation")

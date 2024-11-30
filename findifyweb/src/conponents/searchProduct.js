import React, { useState } from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import TextField from '@mui/material/TextField';
import axios from "axios";
import ListTheProduct from './listTheProduct';
import image from '../loading-animation.gif'

export default function SearchProduct() {
  const [open, setOpen] = useState(false);
  const [minPrice, setMinPrice] = useState('');
  const [maxPrice, setMaxPrice] = useState('');
  const [productName, setProductName] = useState('');
  const [loading, setLoading] = useState(false);
  const [flag, setFlag] = useState(1);
  const [url, setUrl] = useState('');

  const findProduct = async () => {
    setOpen(true); 
    console.log('button clicked');
  };

  const handleClose = () => {
    setOpen(false); 
  };

  const handleSubmit = async () => {
    let apiUrl = 'http://127.0.0.1:8000/';
    setLoading(true); 
    setOpen(false); 
    try {
      const res = await axios.post(apiUrl, {
        priceMin: minPrice,
        priceMax: maxPrice,
        productName: productName,
      });
      setFlag(0);
      setUrl(res.data.url);
      console.log(res);
    } catch (error) {
      console.error('Error fetching product:', error);
    } finally {
      setLoading(false); 
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="text-center">
          <img 
            src={image}
            alt="Loading..." 
            className="w-20 h-20 mx-auto"
          />
          <p className="mt-4 text-lg font-medium text-gray-600">
            Fetching your product details, please wait...
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex flex-col items-center justify-center h-screen space-y-4">
      {flag ? (
        <div>
          <input 
            onChange={(e) => setProductName(e.target.value)} 
            placeholder="searching?" 
            className="p-2 text-black" 
          />
          <Button onClick={findProduct} variant="outlined">
            Find the Product
          </Button>

          <Dialog open={open} onClose={handleClose}>
            <DialogTitle>Enter Price Range</DialogTitle>
            <DialogContent>
              <TextField
                autoFocus
                margin="dense"
                label="Min Price"
                type="number"
                fullWidth
                value={minPrice}
                onChange={(e) => setMinPrice(e.target.value)}
              />
              <TextField
                margin="dense"
                label="Max Price"
                type="number"
                fullWidth
                value={maxPrice}
                onChange={(e) => setMaxPrice(e.target.value)}
              />
            </DialogContent>
            <DialogActions>
              <Button onClick={handleClose} color="primary">
                Cancel
              </Button>
              <Button onClick={handleSubmit} color="primary">
                Submit
              </Button>
            </DialogActions>
          </Dialog>
        </div>
      ) : (
        <ListTheProduct url={url} />
      )}
    </div>
  );
}
